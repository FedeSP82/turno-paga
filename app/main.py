
from fastapi import FastAPI
from app.routes import giorni, mesi

app = FastAPI(title="Turno & Paga CCNL Elettrico")

app.include_router(giorni.router)
app.include_router(mesi.router)

@app.get("/health")
def health():
    return {"status": "ok"}
