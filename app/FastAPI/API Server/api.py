# Import requested libraries
from datetime import datetime, timezone
from fastapi import FastAPI
from Components.bwt_calculator import encoder as bwt

# Create an app istance
app = FastAPI()

# root getter
@app.get("/")
async def root():
    return {
        "position": "/",
        "message": "Hello World!"
    }

# bwt calculator
@app.get("/calculator/{value}")
async def calculator(value: str):
    encoded_string = bwt(value)
    return {
        "original": str(value),
        "encoded": encoded_string
    }

# health checker endpoint
@app.get("/health")
async def read_health():
    return {
        "position": "/health",
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }