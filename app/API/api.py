import sys
import os

# Get absolute path of project directory 
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)                # get project root 
components_path = os.path.join(project_root, 'Components') # get components path

sys.path.insert(0, components_path)
sys.path.insert(0, project_root)

from datetime import datetime, timezone
from fastapi import FastAPI
from Components.bwt_calculator import encoder as bwt

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