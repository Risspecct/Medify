# ⚕️ Medify – AI-Powered Prescription Analyzer

An intelligent healthcare assistant that extracts, analyzes, verifies, and summarizes **medical prescriptions** using AI, machine learning, and cloud services.

---

## 🚀 Features

### 🔍 Prescription Analysis

* **OCR with Google Cloud Vision API**

  * Extracts text from uploaded or captured prescription images.
  * <img width="1855" height="916" alt="Screenshot 2025-08-30 132053" src="https://github.com/user-attachments/assets/37e064de-6b1d-4141-920c-74aa1d40c327" />

* **Biomedical Named Entity Recognition (NER)** with HuggingFace Transformers

  * Identifies **medications, dosages, and symptoms** from free-text prescriptions.
   <img width="1832" height="717" alt="image" src="https://github.com/user-attachments/assets/af707e07-3861-4474-bae8-ba2346945f48" />


### 🧪 Drug Interaction Analysis

* AI-powered backend using **IBM Watson Granite Models**.
* Detects potential **drug–drug interactions** with structured risk levels (🔴 High, 🟡 Moderate, 🟢 Low).
  <img width="1856" height="889" alt="Screenshot 2025-08-30 132157" src="https://github.com/user-attachments/assets/07594fa2-7c80-4a7d-9e68-30cea82bf534" />


### ✅ Prescription Verification

* Matches medications against a curated **dosage dataset**.
* Verifies:

  * **Symptom appropriateness**
  * **Age safety**
  * **Dosage safety (mg/kg)**
 <img width="1853" height="655" alt="Screenshot 2025-08-30 132328" src="https://github.com/user-attachments/assets/e5975448-43ab-4b9e-ade0-689b11e23a3a" />
 <img width="1853" height="659" alt="Screenshot 2025-08-30 132440" src="https://github.com/user-attachments/assets/d9796378-9669-4957-876b-0b492c602b8c" />


### 📊 Dosage Guidelines

* Fetches standardized dosage ranges, intervals, and safety notes from dataset.
* Personalized to **patient’s age and weight**.
<img width="1827" height="706" alt="Screenshot 2025-08-30 132510" src="https://github.com/user-attachments/assets/6947fea7-e958-4cda-82b2-8d97b334793c" />


### 🌿 Alternatives & Remedies

* Suggests **alternative medications**.
* Provides **home remedies** for common conditions from an internal knowledge base.
<img width="1839" height="923" alt="Screenshot 2025-08-30 132546" src="https://github.com/user-attachments/assets/3af8847b-9815-428e-9ab1-db80602371b8" />


### 🤖 AI-Powered Summary

* Generates a **final patient-friendly report** consolidating:

  * Verification results
  * Dosage guidelines
  * Alternative remedies
* Uses **Watson AI summarization** for clear, simple medical summaries.
<img width="1791" height="790" alt="Screenshot 2025-08-30 132625" src="https://github.com/user-attachments/assets/f7d1b27a-2d80-4eb9-8503-69e8bf4d931a" />

---

## 🏗️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
* **AI Models:** HuggingFace Transformers (`d4data/biomedical-ner-all`), IBM Granite (Watson ML)
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
│── app.py                   # Streamlit frontend
│── requirements.txt          # Dependencies
│── .env.example              # Environment variables template
│
├── backend/
│   ├── main.py               # FastAPI entrypoint
│   ├── routers/              # API endpoints
│   ├── data_processors/      # Dosage & prescription validation
│   ├── watson_ai/            # Watson AI integration
│
├── datasets/                 # Dosage + alternative medicine datasets
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repo

```bash
git clone https://github.com/your-username/medify.git
cd medify
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment

Copy `.env.example` → `.env` and set:

```ini
WATSON_API_KEY=your_api_key
WATSON_PROJECT_ID=your_project_id
WATSON_REGION_URL=your_region_url
FAST_API_URL=http://127.0.0.1:8000
DOSAGE_FILE_PATH=datasets/dosage.csv
```

### 5️⃣ Run Backend

```bash
cd backend
uvicorn main:app --reload
```

API will be available at: `http://127.0.0.1:8000/docs`

### 6️⃣ Run Frontend

```bash
streamlit run app.py
```

---

## 📖 Usage Flow

1. Upload a prescription (image, photo, or text).
2. Extract entities (NER + OCR).
3. Run **Drug Interaction Check**.
4. Perform **Manual Verification** with dataset.
5. Fetch **Dosage Guidelines**.
6. Explore **Alternatives & Remedies**.
7. Generate a **Final AI-Powered Summary**.

---

## ⚠️ Disclaimer

This tool is for **educational and research purposes only**.
It is **not a substitute for professional medical advice**.
Always consult a qualified doctor before taking any medication.
