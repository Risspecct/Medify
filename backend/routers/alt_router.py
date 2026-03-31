from fastapi import APIRouter, HTTPException
from utils import alt_service

router = APIRouter()


@router.get("/{med_name}")
def get_alternatives(med_name: str):
    result = alt_service.find_med_and_calculate_savings(med_name)
    if not result:
        raise HTTPException(status_code=404, detail="Medication not found")
    return result
