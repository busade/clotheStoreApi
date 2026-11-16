from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.cart import CartRead, CartItemCreate, CartItemUpdate, CartItemRead
from app.controllers import cart_controller as ctl

router = APIRouter(prefix="/cart", tags=["cart"])

@router.get("", response_model=CartRead)
def get_cart(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ctl.get_cart(user, db)

@router.post("/items", response_model=CartItemRead, status_code=status.HTTP_201_CREATED)
def add_item(payload: CartItemCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ctl.add_to_cart(payload, user, db)

@router.patch("/items/{item_id}", response_model=CartItemRead)
def update_item(item_id: int, payload: CartItemUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ctl.update_cart_item(item_id, payload, user, db)

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(item_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ctl.remove_cart_item(item_id, user, db)

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def clear_cart(db: Session = Depends(get_db), user=Depends(get_current_user)):
    ctl.clear_cart(user, db)
