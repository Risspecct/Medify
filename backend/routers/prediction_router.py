from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.pred import predict

router = APIRouter()

class PredictRequest(BaseModel):
    symptoms: list[str]

@router.post("/")
def predict_disease(request: PredictRequest):
    try:
        result = predict(request.symptoms)
        return {"predictions": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))