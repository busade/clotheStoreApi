from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field
from app.models.order import OrderStatus

class CheckoutRequest(BaseModel):
    shipping_address: str = Field(min_length=5)

class OrderItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int
    unit_price: Decimal

class OrderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    total_amount: Decimal
    status: OrderStatus
    shipping_address: str
    created_at: datetime
    items: list[OrderItemRead]

class OrderStatusUpdate(BaseModel):
    status: OrderStatus
