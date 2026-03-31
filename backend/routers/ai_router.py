from fastapi import APIRouter
from gemini_ai import summarizer, interactions

router = APIRouter()


@router.post("/summarize")
def summarize_text(request: summarizer.SummaryRequest):
    return summarizer.summarize_text(request)


@router.post("/interactions")
def get_interaction_results(request: interactions.InteractionRequest):
    return interactions.get_interaction_results(request)
