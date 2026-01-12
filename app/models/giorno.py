
from pydantic import BaseModel
from typing import Optional

class Giorno(BaseModel):
    data: str
    turno_previsto: str
    turno_effettivo: Optional[str]
    note: Optional[str] = ""
    trasferta_96: bool = False
    trasferta_66: bool = False
    assenza: bool = False
    carburante: float = 0.0
    autostrada: float = 0.0
