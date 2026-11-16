from decimal import Decimal
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_admin
from app.models.product import ProductCategory, ProductSize
from app.schemas.product import ProductRead, ProductCreate, ProductUpdate
from app.controllers import product_controller as ctl

router = APIRouter(prefix="/products", tags=["products"])

@router.get("", response_model=list[ProductRead])
def list_products(category: ProductCategory | None = None, size: ProductSize | None = None, color: str | None = None, min_price: Decimal | None = Query(default=None, ge=0), max_price: Decimal | None = Query(default=None, ge=0), search: str | None = None, limit: int = Query(default=20, ge=1, le=100), offset: int = Query(default=0, ge=0), db: Session = Depends(get_db)):
    return ctl.list_products(db, category, size, color, min_price, max_price, search, limit, offset)

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return ctl.get_product(product_id, db)

@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return ctl.create_product(payload, db)

@router.patch("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, payload: ProductUpdate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return ctl.update_product(product_id, payload, db)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    ctl.delete_product(product_id, db)
