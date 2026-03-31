from fastapi import APIRouter, HTTPException, Body
from utils.ner_processor import extract_medical_entities
from transformers import pipeline


router = APIRouter()

# Load the model once when the router is initialized
try:
    print("Loading Biomedical NER model...")
    ner_pipeline = pipeline(
        "ner",
        model="d4data/biomedical-ner-all",
        aggregation_strategy="simple"
    )
except Exception as e:
    print(f"Warning: NER model failed to load: {e}")
    ner_pipeline = None


@router.post("/parse")
async def parse_medical_text(text: str = Body(..., embed=True)):
    """
    Receives text and returns extracted medical entities.
    """
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required.")

    try:
        entities = extract_medical_entities(text, ner_pipeline)
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
