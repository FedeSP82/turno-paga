
from fastapi import FastAPI
from app.routes import giorni, mesi

app = FastAPI(title="Turno & Paga CCNL Elettrico")

app.include_router(giorni.router)
app.include_router(mesi.router)

@app.get("/health")
def health():
    return {"status": "ok"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "service": "turno-paga backend"}
