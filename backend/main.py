from fastapi import FastAPI
from pydantic import BaseModel
from model import business_feasibility
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for dev)
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods (POST, GET, OPTIONS)
    allow_headers=["*"],
)

class BusinessInput(BaseModel):
    industry: str
    market_size: float
    competition: int
    investment: float
    growth_rate: float

@app.post("/analyze")
def analyze_business(data: BusinessInput):
    result = business_feasibility(
        data.industry,
        data.market_size,
        data.competition,
        data.investment,
        data.growth_rate
    )
    return result
