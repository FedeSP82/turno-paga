from fastapi import APIRouter
from app.storage import GIORNI

router = APIRouter(prefix="/mesi", tags=["mesi"])


@router.get("/{anno}/{mese}")
def get_mese(anno: int, mese: int):
    giorni_mese = []

    for data, giorno in GIORNI.items():
        # accetta sia DD/MM/YYYY che YYYY-MM-DD
        if str(anno) in data and f"/{mese:02d}/" in data or f"-{mese:02d}-" in data:
            giorni_mese.append(giorno)

    return {
        "anno": anno,
        "mese": mese,
        "giorni": sorted(giorni_mese, key=lambda g: g["data"])
    }
