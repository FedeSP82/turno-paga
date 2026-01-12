from fastapi import APIRouter
from app.services.mesi_service import genera_mese

router = APIRouter(prefix="/mesi", tags=["mesi"])

@router.get("/{anno}/{mese}")
def get_mese(anno: int, mese: int):
    return genera_mese(anno, mese)
