from fastapi import APIRouter

# Import domain routers
from app.domains.users.endpoints import router as users_router

# TODO: Complete items domain
# from app.domains.items.endpoints import router as items_router

api_router = APIRouter()

# Include domain routers
api_router.include_router(users_router, prefix="/users", tags=["users"])
# TODO: Complete items domain
# api_router.include_router(items_router, prefix="/items", tags=["items"])
