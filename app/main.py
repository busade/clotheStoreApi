from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from app import models
from app.api.v1.endpoints import auth, products, cart, orders

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

api = APIRouter(prefix="/api/v1")
api.include_router(auth.router)
api.include_router(products.router)
api.include_router(cart.router)
api.include_router(orders.router)
app.include_router(api)
