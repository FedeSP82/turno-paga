from app.core.calcolo_giorno import calcola_giorno

PAGA_ORARIA = 18.23  # valore di prova


def stampa(titolo, risultato):
    print("\n" + "=" * 40)
    print(titolo)
    print("=" * 40)
    for k, v in risultato.items():
        print(k, ":", v)


# =========================
# TEST 1 - NOTTE NORMALE
# =========================
giorno_notte = {
    "data": "02/11/2025",
    "turno_effettivo": "N",
    "ingresso": "23:00",
    "uscita": "07:00",
    "straordinario": {
        "tipo": None,
        "ore": 0
    }
}

ris1 = calcola_giorno(giorno_notte, PAGA_ORARIA)
stampa("TEST 1 - NOTTE NORMALE", ris1)


# =========================
# TEST 2 - RN LAVORATO
# =========================
giorno_rn = {
    "data": "09/11/2025",
    "turno_effettivo": "RN",
    "ingresso": "23:00",
    "uscita": "07:00",
    "straordinario": {
        "tipo": None,
        "ore": 0
    }
}

ris2 = calcola_giorno(giorno_rn, PAGA_ORARIA)
stampa("TEST 2 - RN LAVORATO", ris2)


# =========================
# TEST 3 - RC + SE
# =========================
giorno_rc_se = {
    "data": "16/11/2025",
    "turno_effettivo": "RC",
    "ingresso": "22:00",
    "uscita": "02:00",
    "straordinario": {
        "tipo": "SE",
        "ore": 4
    }
}

ris3 = calcola_giorno(giorno_rc_se, PAGA_ORARIA)
stampa("TEST 3 - RC + SE", ris3)
