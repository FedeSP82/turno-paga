from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import giorni, mesi

app = FastAPI(title="Turno & Paga CCNL Elettrico")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(giorni.router)
app.include_router(mesi.router)


@app.get("/health")
def health():
    return {"status": "ok"}
