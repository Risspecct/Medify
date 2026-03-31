from fastapi import APIRouter, HTTPException
from utils import prescription_service

router = APIRouter()


@router.get("/verify")
async def verify_prescription(
    symptom: str,
    medicine_name: str,
    age_in_months: int,
    given_dosage_mg_per_kg: float
):
    """
    Endpoint to verify prescription safety.
    """
    try:
        report = prescription_service.verify_medication(
            symptom, medicine_name, age_in_months, given_dosage_mg_per_kg
        )
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dosage/{medicine_name}/{age_in_months}")
async def get_dosage_info(medicine_name: str, age_in_months: int):
    """
    Endpoint to fetch dosage guidelines.
    """
    result = prescription_service.fetch_dosage_guidelines(medicine_name, age_in_months)
    if isinstance(result, str) and "not found" in result.lower():
        raise HTTPException(status_code=404, detail=result)
    return result
