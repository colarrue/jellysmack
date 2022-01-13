from fastapi import APIRouter

router = APIRouter()


@router.get("/{episode_id}")
def get_episode(episode_id):
    return 12
