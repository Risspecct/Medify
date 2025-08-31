# features/ner.py
import re
from datasets.ner_dataset import get_dataset

medications, symptoms, dosage_units, frequencies = get_dataset()


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
