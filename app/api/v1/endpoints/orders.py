from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user, get_current_admin
from app.schemas.order import CheckoutRequest, OrderRead, OrderStatusUpdate
from app.controllers import order_controller as ctl

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/checkout", response_model=OrderRead, status_code=201)
def checkout(payload: CheckoutRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ctl.checkout_cart(payload, user, db)

@router.get("", response_model=list[OrderRead])
def list_orders(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ctl.get_user_orders(user, db)

@router.get("/{order_id}", response_model=OrderRead)
def order_detail(order_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ctl.get_order_detail(order_id, user, db)

@router.patch("/{order_id}/status", response_model=OrderRead)
def set_status(order_id: int, payload: OrderStatusUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return ctl.update_order_status(order_id, payload, db)

@router.patch("/{order_id}/cancel", response_model=OrderRead)
def cancel(order_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ctl.cancel_order(order_id, user, db)
