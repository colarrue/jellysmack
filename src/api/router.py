from fastapi import APIRouter

import src.api.endpoints.characters
import src.api.endpoints.comments
import src.api.endpoints.episodes


api_router = APIRouter()
api_router.include_router(src.api.endpoints.characters.router, prefix="/characters")
api_router.include_router(src.api.endpoints.episodes.router, prefix="/episodes")
api_router.include_router(src.api.endpoints.comments.router, prefix="/comments")
