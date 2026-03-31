from data_processors.dosage import get_dosage
from data_processors.prescription import get_report


def verify_medication(symptom: str, med_name: str, age_months: int, dosage_mg_kg: float):
    """
    Business logic for verifying a prescription.
    """
    # Calls the existing logic in data_processors/prescription.py
    return get_report(symptom, med_name, age_months, dosage_mg_kg)


def fetch_dosage_guidelines(med_name: str, age_months: int):
    """
    Business logic for fetching dosage info.
    """
    # Calls the existing logic in data_processors/dosage.py
    return get_dosage(med_name, age_months)
