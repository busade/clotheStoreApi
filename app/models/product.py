import enum
from decimal import Decimal
from sqlalchemy import Boolean, Enum, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class ProductCategory(str, enum.Enum):
    Shirts = "Shirts"
    Trousers = "Trousers"
    Outerwear = "Outerwear"
    Footwear = "Footwear"
class ProductSize(str, enum.Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, default="")
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    category: Mapped[ProductCategory] = mapped_column(Enum(ProductCategory), nullable=False)
    size: Mapped[ProductSize] = mapped_column(Enum(ProductSize), nullable=False)
    color: Mapped[str] = mapped_column(String(80), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    cart_items = relationship("CartItem", back_populates="product")
