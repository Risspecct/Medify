from fastapi import APIRouter
from watson_ai import summarizer

router = APIRouter()


@router.post("/summarize")
def summarize_text(request: summarizer.SummaryRequest):
    return summarizer.summarize_text(request)
