
from fastapi import APIRouter
from app.models.giorno import Giorno

router = APIRouter(prefix="/giorni", tags=["giorni"])

@router.post("/")
def salva_giorno(giorno: Giorno):
    return {"ok": True, "giorno": giorno}
