from fastapi import APIRouter

from src.api.endpoints import characters
from src.api.endpoints import episodes


api_router = APIRouter()
api_router.include_router(characters.router, prefix="/characters")
api_router.include_router(episodes.router, prefix="/episodes")
