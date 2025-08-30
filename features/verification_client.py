import requests
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

API_BASE_URL = os.getenv("FAST_API_URL")  # This will be set by app.py


def call_verify_api(params: dict):
    endpoint = f"{API_BASE_URL}/drug_info/verify"
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the Verification service. Error: {e}")
        return None


def call_dosage_api(med_name: str, age_months: int):
    endpoint = f"{API_BASE_URL}/drug_info/dosage/{med_name}/{age_months}"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the Dosage service. Error: {e}")
        return None
