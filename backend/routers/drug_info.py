from fastapi import APIRouter
from data_processors.dosage import get_dosage

router = APIRouter()


@router.get("/dosage/{medicine_name}/{age_in_months}")
def fetch_dosage(medicine_name: str, age_in_months):
    return get_dosage(medicine_name, int(age_in_months))
