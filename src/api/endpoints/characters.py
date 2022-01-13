from fastapi import APIRouter

router = APIRouter()


@router.get("/{character_id}")
def get_character(character_id):
    return 12
