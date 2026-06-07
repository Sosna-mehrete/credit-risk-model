from fastapi import FastAPI
import joblib
import numpy as np
from pathlib import Path

from .pydantic_models import RiskRequest, RiskResponse

app = FastAPI()

MODEL_PATH = Path("model.pkl")
model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "Credit Risk API"}


@app.post("/predict")
def predict(data: RiskRequest):

    try:
        X = np.array([[
            data.total_amount,
            data.avg_amount,
            data.std_amount,
            data.transaction_count
        ]])

        probability = model.predict_proba(X)[0][1]

        return {"probability": float(probability)}

    except Exception as e:
        return {"error": str(e)}