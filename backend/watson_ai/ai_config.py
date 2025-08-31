from ibm_watson_machine_learning.foundation_models import Model
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()

# Correct keys
my_credentials = {
    "url": os.getenv("WATSON_REGION_URL", "https://us-south.ml.cloud.ibm.com"),
    "apikey": os.getenv("WATSON_API_KEY", "your_api_key_here"),
}
project_id = os.getenv("WATSON_PROJECT_ID", "your_project_id_here")

# --- MODEL CONFIGURATION ---
model_id = "ibm/granite-3-8b-instruct"
model_parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 300,
    "min_new_tokens": 50,
    "repetition_penalty": 1.05
}

# --- INITIALIZE MODEL ---
granite_model = Model(
    model_id=model_id,
    params=model_parameters,
    credentials=my_credentials,
    project_id=project_id
)
