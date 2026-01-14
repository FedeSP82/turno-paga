from fastapi import APIRouter
from app.services.giorni_store import giorni_salvati

router = APIRouter(
    prefix="/giorni",
    tags=["giorni"]
)

@router.post("/")
def salva_giorno(giorno: dict):
    """
    Salva una giornata lavorativa (mock, in memoria).
    """
    giorni_salvati.append(giorno)
    return {
        "ok": True,
        "giorno": giorno
    }


@router.post("/")
def salva_giorno(giorno: Giorno):
    # usiamo la data come chiave
    GIORNI[giorno.data] = giorno.dict()

    return {
        "ok": True,
        "salvato": giorno.data
    }
