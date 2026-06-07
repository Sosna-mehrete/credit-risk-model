from pydantic import BaseModel

class RiskRequest(BaseModel):
    total_amount: float
    avg_amount: float
    std_amount: float
    transaction_count: int

class RiskResponse(BaseModel):
    probability: float
    
    