from decimal import Decimal
from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.models import Product, ProductCategory, ProductSize, User, UserRole
from app.core.security import hash_password

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if not db.query(Product).first():
            db.add_all([
                Product(name="Everyday Tee", description="Soft cotton crew neck", price=Decimal("24.00"), category=ProductCategory.Shirts, size=ProductSize.M, color="Black", stock_quantity=25),
                Product(name="Classic Chinos", description="Straight fit cotton trousers", price=Decimal("59.00"), category=ProductCategory.Trousers, size=ProductSize.L, color="Olive", stock_quantity=12),
                Product(name="Field Jacket", description="Lightweight outer layer", price=Decimal("119.00"), category=ProductCategory.Outerwear, size=ProductSize.M, color="Navy", stock_quantity=8),
                Product(name="Canvas Low Top", description="Everyday canvas footwear", price=Decimal("49.00"), category=ProductCategory.Footwear, size=ProductSize.XL, color="White", stock_quantity=10),
            ])
        if not db.query(User).filter(User.email == "admin@threadcraft.test").first():
            db.add(User(email="admin@threadcraft.test", hashed_password=hash_password("AdminPass123!"), full_name="ThreadCraft Admin", role=UserRole.admin))
        if not db.query(User).filter(User.email == "customer@threadcraft.test").first():
            db.add(User(email="customer@threadcraft.test", hashed_password=hash_password("Customer123!"), full_name="Sample Customer", role=UserRole.customer))
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
