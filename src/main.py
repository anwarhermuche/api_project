from fastapi import FastAPI
from src.api.v1.routes.products import products_router

app = FastAPI()
app.include_router(products_router)
