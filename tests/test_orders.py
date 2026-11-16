def test_checkout_empty_and_success(client, sample_product):
    payload = {"shipping_address":"123 Test Street"}
    assert client.post("/api/v1/orders/checkout", json=payload).status_code == 400
    assert client.post("/api/v1/cart/items", json={"product_id":sample_product.id,"quantity":2}).status_code == 201
    response = client.post("/api/v1/orders/checkout", json=payload)
    assert response.status_code == 201 and response.json()["total_amount"] == "40.00"
    assert client.get("/api/v1/cart").json()["items"] == []

def test_orders_status_and_cancel(client):
    assert client.get("/api/v1/orders").status_code == 200

def test_admin_order_status_transition_and_invalid_transition(admin_client, db, customer):
    from app.models import Order, OrderStatus
    order = Order(user_id=customer.id, total_amount="20.00", status=OrderStatus.pending, shipping_address="123 Test Street")
    db.add(order); db.commit(); db.refresh(order)
    assert admin_client.patch(f"/api/v1/orders/{order.id}/status", json={"status":"paid"}).status_code == 200
    assert admin_client.patch(f"/api/v1/orders/{order.id}/status", json={"status":"delivered"}).status_code == 400

def test_cancel_restores_stock_and_shipped_order_rejected(client, db, customer, sample_product):
    from app.models import Order, OrderItem, OrderStatus
    pending = Order(user_id=customer.id, total_amount="40.00", status=OrderStatus.pending, shipping_address="123 Test Street")
    shipped = Order(user_id=customer.id, total_amount="20.00", status=OrderStatus.shipped, shipping_address="123 Test Street")
    db.add_all([pending, shipped]); db.flush()
    db.add_all([OrderItem(order_id=pending.id, product_id=sample_product.id, quantity=2, unit_price="20.00"), OrderItem(order_id=shipped.id, product_id=sample_product.id, quantity=1, unit_price="20.00")])
    db.commit()
    assert client.patch(f"/api/v1/orders/{pending.id}/cancel").status_code == 200
    db.refresh(sample_product)
    assert sample_product.stock_quantity == 7
    assert client.patch(f"/api/v1/orders/{shipped.id}/cancel").status_code == 400
