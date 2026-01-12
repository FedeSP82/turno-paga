
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

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "service": "turno-paga backend"}
