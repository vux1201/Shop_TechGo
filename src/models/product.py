from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from db.base_model import Base


class Product(Base):
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str]
    sku: Mapped[str] = mapped_column(String(255))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
