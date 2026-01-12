from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import giorni, mesi

app = FastAPI(title="Turno & Paga CCNL Elettrico")

# CORS (necessario per il frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
app.include_router(giorni.router)
app.include_router(mesi.router)

# HEALTH
@app.get("/health")
def health():
    return {"status": "ok"}

# ROOT
@app.get("/")
def root():
    return {"status": "ok", "service": "turno-paga backend"}

