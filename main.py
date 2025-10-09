# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(title="Trading Webhooks")

# --- health -------------------------------------------------
@app.get("/health")
def health():
    return {"ok": True}

# --- model for fills ---------------------------------------
class Fill(BaseModel):
    timestamp: datetime
    event: str = Field(..., description="e.g., FILL")
    broker: str = Field(..., description="QC_IBKR / IBKR / QC")
    order_id: str
    symbol: str
    side: str  # BUY / SELL
    qty: float
    avg_price: float

# --- fills webhook -----------------------------------------
@app.post("/fills")
async def fills(f: Fill, request: Request):
    # Minimal ack; you can persist to DB or forward later
    payload = f.dict()
    payload["source_ip"] = request.client.host
    return {"ok": True, "received": payload}

# --- (optional) alerts webhook ------------------------------
class Alert(BaseModel):
    timestamp: datetime
    level: str
    message: str

@app.post("/alerts")
async def alerts(a: Alert):
    return {"ok": True, "received": a.dict()}
