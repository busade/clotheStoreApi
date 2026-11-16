from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product

def list_products(db: Session, category=None, size=None, color=None, min_price=None, max_price=None, search=None, limit=20, offset=0):
    """Working public catalog list; add optional filters and pagination behavior."""
    # TODO extension: apply category, size, color, price-range, and search filters.
    return db.query(Product).filter(Product.is_active.is_(True)).offset(offset).limit(limit).all()

def get_product(product_id: int, db: Session):
    product = db.query(Product).filter(Product.id == product_id, Product.is_active.is_(True)).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def create_product(payload, db: Session):
    """TODO: Create an active catalog product from validated admin input."""
    # TODO 1: Map payload fields to Product; add, commit, refresh, and return.
    raise HTTPException(status_code=501, detail="Not implemented")

def update_product(product_id: int, payload, db: Session):
    """TODO: Apply supplied fields to an existing product."""
    # TODO 1: Find active product or return 404.
    # TODO 2: Apply only explicitly provided fields; commit and refresh.
    raise HTTPException(status_code=501, detail="Not implemented")

def delete_product(product_id: int, db: Session):
    """TODO: Soft-delete product by setting is_active=False."""
    # TODO 1: Find product or return 404; set inactive and commit.
    raise HTTPException(status_code=501, detail="Not implemented")
