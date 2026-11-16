from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.cart import CartItem

def get_cart(current_user, db: Session):
    """Working reference: return the current user's cart rows and item count."""
    items = db.query(CartItem).filter(CartItem.user_id == current_user.id).all()
    return {"items": items, "total_items": sum(item.quantity for item in items)}

def add_to_cart(payload, current_user, db: Session):
    """TODO: Add a product, merge duplicate rows, and enforce available stock."""
    # TODO 1: Load active product; return 404 if missing.
    # TODO 2: Find existing user/product row and calculate resulting quantity.
    # TODO 3: Reject quantity above stock with 400; save and return row.
    raise HTTPException(status_code=501, detail="Not implemented")

def update_cart_item(item_id: int, payload, current_user, db: Session):
    """TODO: Set quantity or remove owned row when quantity is zero."""
    # TODO 1: Find item belonging to current user or return 404.
    # TODO 2: Check requested amount against product stock; persist or delete.
    raise HTTPException(status_code=501, detail="Not implemented")

def remove_cart_item(item_id: int, current_user, db: Session):
    """TODO: Remove one cart item belonging to the current user."""
    # TODO 1: Find owned row, return 404 if absent, delete and commit.
    raise HTTPException(status_code=501, detail="Not implemented")

def clear_cart(current_user, db: Session):
    """TODO: Delete all cart rows belonging to the current user."""
    # TODO 1: Delete user's rows and commit.
    raise HTTPException(status_code=501, detail="Not implemented")
