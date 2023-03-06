from fastapi import APIRouter

from apis import brands, categories, discounts, login, products, users

api_router = APIRouter()

api_router.include_router(users.router)
api_router.include_router(login.router)
api_router.include_router(products.router)
api_router.include_router(categories.router)
api_router.include_router(brands.router)
api_router.include_router(brands.router)
api_router.include_router(discounts.router)
