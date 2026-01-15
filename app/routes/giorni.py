from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
import json
from pathlib import Path

router = APIRouter(prefix="/giorni", tags=["giorni"])

DATA_FILE = Path("data_giorni.json")


# ===== MODELLI =====

class Trasferta(BaseModel):
    forfettario: bool = False
    pranzo: bool = False
    benzina: float = 0.0
    autostrada: float = 0.0


class Giorno(BaseModel):
    data: str
    pt: str
    eff: Optional[str] = None
    trasferimento: bool = False
    trasferta: Trasferta


# ===== UTILS =====

def carica_giorni() -> List[dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def salva_giorni(giorni: List[dict]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(giorni, f, ensure_ascii=False, indent=2)


# ===== ROUTES =====

@router.post("/")
def salva_giorno(giorno: Giorno):
    giorni = carica_giorni()

    # rimuove eventuale giorno con stessa data
    giorni = [g for g in giorni if g["data"] != giorno.data]

    giorni.append(giorno.dict())
    salva_giorni(giorni)

    return {"ok": True, "giorno": giorno}


@router.get("/")
def lista_giorni():
    return carica_giorni()
