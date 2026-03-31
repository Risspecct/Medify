import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_BASE_URL = os.getenv("FAST_API_URL", "http://backend:8000")


def ocr_extract(file):
    files = {"file": (file.name, file.getvalue(), file.type)}
    res = requests.post(f"{API_BASE_URL}/ocr/extract", files=files)
    res.raise_for_status()
    return res.json()


def ner_parse(text: str):
    res = requests.post(f"{API_BASE_URL}/ner/parse", json={"text": text})
    res.raise_for_status()
    return res.json()


def predict_disease(symptoms: list):
    res = requests.post(f"{API_BASE_URL}/prediction/", json={"symptoms": symptoms})
    res.raise_for_status()
    return res.json()


def get_interactions(meds: list):
    res = requests.post(f"{API_BASE_URL}/ai/interactions", json={"medicines": meds})
    res.raise_for_status()
    return res.json()


def verify_prescription(symptom, med_name, age_months, dosage_mg_kg):
    params = {
        "symptom": symptom, "medicine_name": med_name, 
        "age_in_months": age_months, "given_dosage_mg_per_kg": dosage_mg_kg
    }
    res = requests.get(f"{API_BASE_URL}/drug_info/verify", params=params)
    res.raise_for_status()
    return res.json()


def get_dosage(med_name, age_months):
    res = requests.get(f"{API_BASE_URL}/drug_info/dosage/{med_name}/{age_months}")
    res.raise_for_status()
    return res.json()


def get_alternatives(med_name):
    res = requests.get(f"{API_BASE_URL}/alternatives/{med_name}")
    if res.status_code == 404: 
        return None
    res.raise_for_status()
    return res.json()


def generate_summary(outputs_list: list):
    res = requests.post(f"{API_BASE_URL}/ai/summarize", json={"outputs": outputs_list})
    res.raise_for_status()
    return res.json()