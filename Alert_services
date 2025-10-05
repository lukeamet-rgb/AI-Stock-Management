from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Alert(BaseModel):
    time: str
    code: str
    details: dict
    equity: float
    gross_exposure_pct: float
    net_exposure_pct: float

@app.get("/health")
def health():
    return {"ok": True, "time": datetime.utcnow().isoformat()+"Z"}

@app.post("/alerts")
def alerts(a: Alert):
    print("ALERT:", a.model_dump())
    return {"ok": True, "received_at": datetime.utcnow().isoformat()+"Z"}
