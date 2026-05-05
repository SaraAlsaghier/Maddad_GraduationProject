from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/game", tags=["game"]) 

class GameLevelData(BaseModel):
    child_id: int
    game_name: str
    level: int

@router.post("/progress")
def receive_game_data(data: GameLevelData):
    print("Level received:", data)
    return {"message": "Level saved"}
