from pydantic import BaseModel
from typing import List
from .giorno import Giorno

class Mese(BaseModel):
    anno: int
    mese: int
    giorni: List[Giorno]
