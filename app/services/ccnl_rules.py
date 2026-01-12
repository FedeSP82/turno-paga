def is_giornata_lavorata(eff: str | None) -> bool:
    if eff is None:
        return False
    return eff not in ["RC", "RN", "R"]


def calcola_trasferimento(eff: str | None) -> bool:
    return is_giornata_lavorata(eff)


def notturno_76(eff: str | None) -> bool:
    return eff == "N"
