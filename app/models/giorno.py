from pydantic import BaseModel
from typing import Optional

class Trasferta(BaseModel):
    forfettario: bool = False
    pranzo: bool = False
    benzina: float = 0.0
    autostrada: float = 0.0

class Giorno(BaseModel):
    data: str
    pt: Optional[str] = None
    eff: Optional[str] = None
    trasferimento: bool = False
    trasferta: Trasferta = Trasferta()
