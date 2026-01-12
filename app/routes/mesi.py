
from fastapi import APIRouter

router = APIRouter(prefix="/mesi", tags=["mesi"])

@router.get("/{anno}/{mese}")
def get_mese(anno: int, mese: int):
    return {"anno": anno, "mese": mese}
