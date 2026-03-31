import time
from typing import Any
from pydantic import BaseModel
from gemini_ai import ai_config
from fastapi import HTTPException
from logger_config import setup_logger

logger = setup_logger("AI_Summarizer")


class SummaryRequest(BaseModel):
    outputs: list[dict[str, Any]]


text = prompt = """
You are a medical assistant summarizer.
I will provide multiple JSON objects from different checks on a prescription:
1. Verification result (symptom check, age check, dosage check, notes, disclaimer)
2. Dosage guidelines
3. Alternative medication / remedies

Task:
- Summarize all the information into 1–2 short paragraphs.
- Use plain, simple language for the general public.
- Highlight whether the prescription seems appropriate or if there are risks.
- Include safe dosage intervals and limits if provided.
- Suggest alternatives or remedies if available.
- Always end with a disclaimer that this is not medical advice and a doctor should be consulted.

Here is the data to summarize:
"""


def refine_input(request) -> str:
    """
    Refine the input text to create a prompt suitable for the model.
    """
    texts = []
    for i, item in enumerate(request.outputs, start=1):
        texts.append(f"Result {i}:\n{item}")
    return "\n\n".join(texts)


def summarize_text(request: SummaryRequest):
    start_time = time.time()
    """
    Summarize the input text using the Gemini model.
    """
    logger.info(f"Received summarization request for {len(request.outputs)} items.")
    prompt = text + refine_input(request)
    try:
        response = ai_config.gemini_model.generate_text(prompt)
        duration = time.time() - start_time
        logger.info(f"AI Summary Success | Latency: {duration:.2f}s")
        return response
    except Exception as e:
        logger.error(f"AI Summary Failed | Error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=502, detail="AI service error; check server logs for details.")
