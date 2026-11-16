def test_catalog_pagination_and_filter(client, sample_product):
    response = client.get("/api/v1/products?category=Shirts&limit=1&offset=0")
    assert response.status_code == 200 and len(response.json()) == 1

def test_product_detail_and_missing(client, sample_product):
    assert client.get(f"/api/v1/products/{sample_product.id}").status_code == 200
    assert client.get("/api/v1/products/999").status_code == 404

def test_admin_create_and_customer_forbidden(admin_client, customer_client):
    payload = {"name":"New Shirt", "description":"", "price":"30.00", "category":"Shirts", "size":"M", "color":"Red", "stock_quantity":3}
    assert admin_client.post("/api/v1/products", json=payload).status_code == 201
    assert customer_client.post("/api/v1/products", json=payload).status_code == 403

def test_product_patch_delete(admin_client, sample_product):
    assert admin_client.patch(f"/api/v1/products/{sample_product.id}", json={"name":"Updated"}).status_code == 200
    assert admin_client.delete(f"/api/v1/products/{sample_product.id}").status_code == 204
