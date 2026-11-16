from pydantic import BaseModel, ConfigDict, Field
from app.schemas.product import ProductRead

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class CartItemUpdate(BaseModel):
    quantity: int = Field(ge=0)

class CartItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int
    product: ProductRead

class CartRead(BaseModel):
    items: list[CartItemRead]
    total_items: int
