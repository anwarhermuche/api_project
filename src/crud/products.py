from sqlalchemy.orm import Session
from src.schemas.product import Product as ProductSchema
from src.models.product import Product as ProductModel
from typing import List


class ProductCrud:
    def __init__(self, db: Session):
        self.db = db

    def get_products(self) -> List[ProductModel]:
        return self.db.query(ProductModel).all()

    def get_product_by_id(self, product_id: int) -> ProductModel | None:
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()

    def create_product(self, product: ProductSchema) -> ProductModel:
        new_product = ProductModel(**product.model_dump())
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def update_product(
        self, product_id: int, new_product: ProductSchema
    ) -> ProductModel | None:
        product = self.get_product_by_id(product_id)
        if product:
            product.name = new_product.name  # type: ignore
            product.price = new_product.price  # type: ignore
            product.description = new_product.description  # type: ignore
            self.db.commit()
            return product
        return None

    def delete_product(self, product_id: int) -> bool:
        product = self.get_product_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False
