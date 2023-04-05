from sqlalchemy import select, Select
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.product import Brand, Category, Discount, Product, ProductVariant
from schemas import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def get_multi_filter(
        self,
        category_id: list[int] | None = None,
        brand_id: list[int] | None = None,
        keyword: str | None = None,
    ) -> Select[tuple[Product]]:
        stmt = select(Product)
        if category_id:
            stmt = stmt.where(Product.category_id.in_(category_id))
        if brand_id:
            stmt = stmt.where(Product.brand_id.in_(brand_id))
        if keyword:
            stmt = stmt.where(Product.name.icontains(keyword))
        return stmt


product = CRUDProduct(Product)
