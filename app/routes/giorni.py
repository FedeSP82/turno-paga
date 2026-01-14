from fastapi import APIRouter
from pydantic import BaseModel
from app.storage import GIORNI

router = APIRouter(prefix="/giorni", tags=["giorni"])


class Trasferta(BaseModel):
    forfettario: bool
    pranzo: bool
    benzina: float
    autostrada: float


class Giorno(BaseModel):
    data: str          # "YYYY-MM-DD" o "DD/MM/YYYY"
    pt: str
    eff: str | None
    trasferimento: bool
    trasferta: Trasferta


@router.post("/")
def salva_giorno(giorno: Giorno):
    # usiamo la data come chiave
    GIORNI[giorno.data] = giorno.dict()

    return {
        "ok": True,
        "salvato": giorno.data
    }
