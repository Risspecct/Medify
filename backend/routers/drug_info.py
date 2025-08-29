from fastapi import APIRouter
from data_processors.dosage import get_dosage
from data_processors.prescription import get_report

router = APIRouter()


@router.get("/dosage/{medicine_name}/{age_in_months}")
def fetch_dosage(medicine_name: str, age_in_months):
    return get_dosage(medicine_name, int(age_in_months))


@router.get("/verify")
def verify_prescription(symptom: str, medicine_name: str, age_in_months: int, given_dosage_mg_per_kg: float):
    return get_report(symptom, medicine_name, age_in_months, given_dosage_mg_per_kg)
