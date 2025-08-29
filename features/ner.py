# features/ner.py

import re

# --- DATA LISTS (The project's "knowledge base") ---
# This file contains the pure Python logic and data for NER.
medications = [
    "aspirin", "amoxicillin", "paracetamol", "ibuprofen", "lisinopril", "ondansetron",
    "omeprazole", "atorvastatin", "warfarin", "albuterol", "metformin", "azithromycin",
    "doxycycline", "ceftriaxone", "cetirizine", "pantoprosole", "levocetirizine",
    "domperidone", "diclofenac", "losartan", "amlodipine", "montelukast", "clopidogrel",
    "zoloft", "cough syrup", "dolo 650", "crocin", "calpol", "combiflam", "meftal p",
    "meftal spas", "okacet", "alerid", "azee", "levolin", "betadine", "sinarest",
    "asthalin", "ventolin", "thyronorm", "ecosprin", "shelcal", "becosules", "revital"
]

symptoms = [
    "fever", "headache", "chest pain", "sore throat", "cold", "cough", "stomach pain",
    "vomiting", "loose motion", "diarrhea", "acidity", "gas", "heartburn", "nausea",
    "fatigue", "weakness", "shortness of breath", "migraine", "jaundice", "malaria",
    "dengue", "high blood pressure", "diabetes", "anxiety", "high cholesterol",
    "flu symptoms", "body aches", "dizzy"
]

dosage_units = [
    "mg", "g", "ml", "mcg", "units", "puffs", "drops", "sachets",
    "tablet", "tablets", "capsule", "capsules", "pill", "pills",
    "injection", "injections", "ampoule", "vial"
]

frequencies = [
    "daily", "once a day", "twice a day", "three times a day", "four times a day",
    "od", "bid", "tds", "qid", "hs", "prn", "as needed", "stat", "immediately",
    "every morning", "every evening", "before breakfast", "after meals", "at bedtime",
    r'every\s*(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s*hours'
]


def extract_medical_entities(text: str, ner_pipeline_func) -> dict:
    """
    Uses a robust "find and consume" strategy with rules first, then NER as a fallback.
    This function is completely independent of Streamlit.

    Args:
        text: The input text to analyze.
        ner_pipeline_func: A pre-loaded Hugging Face NER pipeline object.

    Returns:
        A dictionary containing the extracted entities.
    """
    remaining_text = text.lower()
    cleaned_entities = {"Medication": [], "Dosage": [], "Frequency": [], "Symptoms": []}

    # Step 1: Find and Consume Medications (High Priority)
    for med in sorted(medications, key=len, reverse=True):
        match = re.search(r'\b' + re.escape(med) + r'\b', remaining_text)
        if match:
            cleaned_entities["Medication"].append(med)
            remaining_text = remaining_text.replace(match.group(0), "", 1)

    # Step 2: Find and Consume Frequencies
    for freq in sorted(frequencies, key=len, reverse=True):
        match = re.search(r'\b' + freq + r'\b', remaining_text, re.IGNORECASE)
        if match:
            cleaned_entities["Frequency"].append(match.group(0))
            remaining_text = remaining_text.replace(match.group(0), "", 1)

    # Step 3: Find and Consume Dosages
    num_words = "one|two|three|four|five|six|seven|eight|nine|ten"
    dosage_pattern = re.compile(r'\b(\d+|' + num_words + r')\s*(' + '|'.join(dosage_units) + r's?)\b', re.IGNORECASE)
    matches = dosage_pattern.finditer(remaining_text)
    for match in matches:
        cleaned_entities["Dosage"].append(match.group(0))
        remaining_text = remaining_text.replace(match.group(0), "", 1)

    # Step 4: Find and Consume Symptoms from what is left
    for sym in sorted(symptoms, key=len, reverse=True):
         match = re.search(r'\b' + re.escape(sym) + r'\b', remaining_text)
         if match:
            cleaned_entities["Symptoms"].append(sym)
            remaining_text = remaining_text.replace(match.group(0), "", 1)

    # Step 5: (Fallback) Use NER on the original text to find anything missed
    if not cleaned_entities["Medication"]:
        ner_results = ner_pipeline_func(text)
        for entity in ner_results:
            word = entity['word'].lower().strip()
            if entity['entity_group'] in ["Drug", "Medicine"]:
                if len(word) > 3 and word not in ["medication", "prescription"]:
                     cleaned_entities["Medication"].append(word)

    # Final Cleanup - MUST RETURN the data
    for key in cleaned_entities:
        cleaned_entities[key] = sorted(list(set(item.strip() for item in cleaned_entities[key])))

    return cleaned_entities