def test_get_cart(client):
    assert client.get("/api/v1/cart").status_code == 200

def test_add_merge_and_stock_limit(client, sample_product):
    payload = {"product_id": sample_product.id, "quantity": 1}
    assert client.post("/api/v1/cart/items", json=payload).status_code == 201
    assert client.post("/api/v1/cart/items", json=payload).status_code == 201
    assert client.post("/api/v1/cart/items", json={"product_id":sample_product.id,"quantity":100}).status_code == 400

def test_update_and_remove_item(client, sample_product):
    item = client.post("/api/v1/cart/items", json={"product_id":sample_product.id,"quantity":1}).json()
    assert client.patch(f"/api/v1/cart/items/{item['id']}", json={"quantity":2}).status_code == 200
    assert client.delete(f"/api/v1/cart/items/{item['id']}").status_code == 204
