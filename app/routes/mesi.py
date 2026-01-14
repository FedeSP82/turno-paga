from fastapi import APIRouter
from app.services.giorni_store import giorni_salvati

router = APIRouter(prefix="/mesi", tags=["mesi"])

@router.get("/{anno}/{mese}")
def get_mese(anno: int, mese: int):
    giorni_mese = [
        g for g in giorni_salvati
        if g["data"].endswith(f"/{mese:02d}/{anno}")
    ]

    return {
        "anno": anno,
        "mese": mese,
        "giorni": giorni_mese
    }
