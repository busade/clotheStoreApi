from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field
from app.models.product import ProductCategory, ProductSize

class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str = ""
    price: Decimal = Field(gt=0)
    category: ProductCategory
    size: ProductSize
    color: str
    stock_quantity: int = Field(ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = Field(default=None, gt=0)
    category: ProductCategory | None = None
    size: ProductSize | None = None
    color: str | None = None
    stock_quantity: int | None = Field(default=None, ge=0)

class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    is_active: bool
