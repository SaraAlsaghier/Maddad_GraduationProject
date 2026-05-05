from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, GameProgress  # لازم يكون عندك مودل
from app.routers.auth import _get_current_user

router = APIRouter(prefix="/api/game", tags=["game"])

class LevelData(BaseModel):
    level: int

@router.post("/progress")
def save_progress(
    data: LevelData,
    current_user: User = Depends(_get_current_user),  # 🔥 يجيب child_id
    db: Session = Depends(get_db)
):
    new_progress = GameProgress(
        user_id=current_user.id,   # 🔥 من الداتابيس
        level=data.level
    )

    db.add(new_progress)
    db.commit()

    return {"message": "Level saved"}
