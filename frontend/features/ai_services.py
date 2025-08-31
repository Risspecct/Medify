import requests
import streamlit as st
from typing import List, Dict, Any
from dotenv import load_dotenv
import os
load_dotenv()

# The base URL will be set by app.py
API_BASE_URL = os.getenv("FAST_API_URL")


def call_interaction_api(medicines: List[str]) -> str:
    """
    Calls the new FastAPI backend to get a formatted interaction report.
    Matches: POST /ai/interactions
    """
    if not medicines or len(medicines) < 2:
        return "Please extract at least two medications to check for interactions."

    endpoint = f"{API_BASE_URL}/ai/interactions"
    # The backend Pydantic model expects the key "medicines"
    payload = {"medicines": medicines}

    try:
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        # The backend returns the raw text from the LLM, which requests decodes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the AI Interaction service. Is the backend running? Error: {e}")
        return "Interaction analysis could not be performed due to a connection error."


def call_summary_api(analysis_data: Dict[str, Any]) -> str:
    """
    Calls the new FastAPI backend to generate an AI-powered summary.
    Matches: POST /ai/summarize
    """
    endpoint = f"{API_BASE_URL}/ai/summarize"

    # The backend Pydantic model expects a key "outputs" which is a list of dictionaries
    outputs_list = []
    if "ner_results" in analysis_data:
        outputs_list.append({"Extracted Entities": analysis_data["ner_results"]})
    if "interaction_report" in analysis_data:
        outputs_list.append({"Interaction Analysis": analysis_data["interaction_report"]})
    # Add other results here if needed

    if not outputs_list:
        return "No analysis has been performed yet. Please extract entities first."

    payload = {"outputs": outputs_list}

    try:
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        # The backend returns the raw text from the LLM
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the AI Summarizer service. Is the backend running? Error: {e}")
        return "Summary could not be generated due to a connection error."
