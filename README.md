# ⚕️ Medify – AI-Powered Prescription Analyzer

<!-- Badges Section -->

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python 3.11">
  <img src="https://img.shields.io/badge/Framework-Streamlit%20%7C%20FastAPI-success" alt="Framework">
  <img src="https://img.shields.io/badge/AI-HuggingFace%20%7C%20IBM%20Watson-purple" alt="AI Models">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License: MIT">
</p>

An intelligent healthcare assistant that extracts, analyzes, verifies, and summarizes medical prescriptions using AI, machine learning, and cloud services.

---

## 🚀 Features

### 🔍 Prescription Analysis & NER

Extracts text from prescription images using **Google Cloud Vision API** and identifies key medical entities like medications, dosages, and symptoms using a **HuggingFace Biomedical NER model**.


---

### 🧪 AI-Powered Drug Interaction Analysis

* AI-powered backend using **Google Gemini (Generative AI)**.
* Detects potential **drug–drug interactions** with structured risk levels (🔴 High, 🟡 Moderate, 🟢 Low).
  <img width="1856" height="889" alt="Screenshot 2025-08-30 132157" src="https://github.com/user-attachments/assets/07594fa2-7c80-4a7d-9e68-30cea82bf534" />


### ✅ Prescription Verification

Cross-references prescription details against a curated medical dataset to verify:

* **Symptom Appropriateness**: Checks if the medication is a valid treatment for the indicated symptom.
* **Age Safety**: Ensures the patient's age is within the recommended range for the drug.
* **Dosage Safety**: Validates the prescribed dosage (in mg/kg) against safe limits.

---

### 📊 Personalized Dosage Guidelines

Fetches standardized dosage ranges, intervals, and critical safety notes for a given medication, personalized to the patient’s age.

---

### 🌿 Alternatives & Home Remedies

Suggests alternative medications and provides relevant home remedies for common conditions, sourced from an internal knowledge base.

---

### 🤖 AI-Powered Summary

* Generates a **final patient-friendly report** consolidating:

  * Verification results
  * Dosage guidelines
  * Alternative remedies
* Uses **Google Gemini summarization** for clear, simple medical summaries.
<img width="1791" height="790" alt="Screenshot 2025-08-30 132625" src="https://github.com/user-attachments/assets/f7d1b27a-2d80-4eb9-8503-69e8bf4d931a" />

---

## 🏗️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
* **AI Models:** HuggingFace Transformers (`d4data/biomedical-ner-all`), Google Gemini (Generative AI)
* **OCR:** Google Cloud Vision API
* **Dataset:** `dosage.csv` + curated alternative medicines dataset
* **Other Libraries:**

  * `pandas` for data processing
  * `requests` for API calls
  * `dotenv` for environment management

---

## 📂 Project Structure

```
medify/
├── README.md
├── docker-compose.yml
├── render.yaml
├── .env.example
│
<<<<<<< Updated upstream
├── backend/                # FastAPI backend
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py             # Entry point for backend
│   ├── data_processors/    # Data preprocessing utilities
│   │   ├── dosage.py
│   │   └── prescription.py
│   ├── routers/            # API routes
│   │   ├── ai_router.py
│   │   └── drug_info.py
│   └── watson_ai/          # IBM Watson AI integration
│       ├── ai_config.py
│       ├── interactions.py
│       └── summarizer.py
=======
├── backend/
│   ├── main.py               # FastAPI entrypoint
│   ├── routers/              # API endpoints
│   ├── data_processors/      # Dosage & prescription validation
│   ├── watson_ai/            # Gemini AI integration (Gemini client lives here)
>>>>>>> Stashed changes
│
├── datasets/               # Project datasets
│   ├── alt_dataset.py
│   ├── dosage.csv
│   └── ner_dataset.py
│
└── frontend/               # Streamlit/Frontend app
    ├── Dockerfile
    ├── requirements.txt
    ├── app.py              # Entry point for frontend
    └── features/           # Core frontend features
        ├── ai_services.py
        ├── alternative.py
        ├── ner.py
        ├── ocr.py
        └── verification_client.py
```

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Risspecct/Medify.git
cd medify
```

### 2. Configure Environment Variables

Copy the example environment file and fill in your API keys and configuration details.

```bash
cp .env.example .env
```

Update the `.env` file with your credentials:

```env
# For backend/main.py
WATSON_API_KEY="your_watson_api_key"
WATSON_PROJECT_ID="your_watson_project_id"
WATSON_URL="your_watson_region_url"
DOSAGE_FILE_PATH="datasets/dosage.csv"

# For frontend/app.py
FAST_API_URL="http://127.0.0.1:8000"
GCP_SERVICE_ACCOUNT_JSON='{...your_gcp_json...}'
```

### 3. Run with Docker Compose (Recommended)

This is the easiest way to start both the frontend and backend services.

```bash
docker-compose up --build
```

* **Streamlit Frontend**: [http://localhost:8501](http://localhost:8501)
* **FastAPI Backend Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 4. Manual Local Installation (Without Docker)

<details>
<summary>Click to view manual setup instructions</summary>

#### a. Create a Virtual Environment

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### b. Install Dependencies

Install dependencies for both the frontend and backend:

```bash
pip install -r frontend/requirements.txt
pip install -r backend/requirements.txt
```

### 4️⃣ Configure Environment

Copy `.env.example` → `.env` and set:

```ini
GENAI_API_KEY=your_genai_api_key
GEMINI_MODEL_ID=models/gemini-1.5
FAST_API_URL=http://127.0.0.1:8000
DOSAGE_FILE_PATH=datasets/dosage.csv
```

### 5️⃣ Run Backend

```bash
cd backend
uvicorn main:app --reload
```

#### d. Run the Frontend Application

```bash
streamlit run frontend/app.py
```

</details>

---

## 📖 Usage Flow

1. **Upload Prescription**: Start by uploading an image, taking a photo, or pasting text from a prescription.
2. **Extract Entities**: OCR + NER to identify medications, symptoms, and dosages.
3. **Check Drug Interactions**: AI-powered interaction risk check.
4. **Verify Prescription**: Validate symptoms, age safety, and dosage.
5. **Fetch Guidelines**: Get standardized dosage info.
6. **Find Alternatives**: Explore alternatives & home remedies.
7. **Generate Summary**: AI-generated, patient-friendly report.

---

## ⚠️ Disclaimer

This tool is for **educational and research purposes only**.
It is **not a substitute for professional medical advice**.
Always consult a qualified doctor before making any healthcare decisions.
