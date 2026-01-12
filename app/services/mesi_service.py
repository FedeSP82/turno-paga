from app.models.mese import Mese
from app.models.giorno import Giorno

def genera_mese(anno: int, mese: int) -> Mese:
    # PER ORA: mock semplice
    giorni = [
        Giorno(
            data="01/11/2025",
            pt="N",
            eff="N",
            trasferimento=True
        )
    ]

    return Mese(
        anno=anno,
        mese=mese,
        giorni=giorni
    )
