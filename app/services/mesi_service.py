from app.models.mese import Mese
from app.models.giorno import Giorno
from app.services.ccnl_rules import calcola_trasferimento

def genera_mese(anno: int, mese: int) -> Mese:
    giorni_raw = [
        {"data": "01/11/2025", "pt": "N", "eff": "N"},
        {"data": "02/11/2025", "pt": "RC", "eff": None},
    ]

    giorni = []
    for g in giorni_raw:
        giorni.append(
            Giorno(
                data=g["data"],
                pt=g["pt"],
                eff=g["eff"],
                trasferimento=calcola_trasferimento(g["eff"])
            )
        )

    return Mese(anno=anno, mese=mese, giorni=giorni)
