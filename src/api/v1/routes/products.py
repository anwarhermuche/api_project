from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from src.crud.products import ProductCrud
from src.schemas.product import Product, ProductRead
from typing import List

from src.db.engine import get_db
from sqlalchemy.orm import Session

products_router = APIRouter(prefix="/api/v1/products", tags=["products"])


@products_router.get("/", response_model=List[ProductRead])
async def get_products(db: Session = Depends(get_db)):
    product_crud = ProductCrud(db)
    return product_crud.get_products()


@products_router.get("/{product_id}", response_model=ProductRead)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product_crud = ProductCrud(db)
    product = product_crud.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@products_router.post("/", response_model=ProductRead)
async def create_product(product: Product, db: Session = Depends(get_db)):
    product_crud = ProductCrud(db)
    return product_crud.create_product(product)


@products_router.put("/{product_id}", response_model=ProductRead)
async def update_product(
    product_id: int, product: Product, db: Session = Depends(get_db)
):
    product_crud = ProductCrud(db)
    product_updated = product_crud.update_product(product_id, product)
    if product_updated is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_updated


@products_router.delete("/{product_id}", response_model=None)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_crud = ProductCrud(db)
    if product_crud.delete_product(product_id):
        return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Product not found")
