import os

from fastapi import FastAPI
from routers.drug_info import router as drug_info_router
from routers.ai_router import router as ai_router
from routers.ocr_router import router as ocr_router
from routers.ner_router import router as ner_router
from routers.alt_router import router as alt_router
from routers.prediction_router import router as prediction_router
import uvicorn
import logging
from data_processors.prescription import dosage_file_path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("medify_debug.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("Medify")

app = FastAPI()

app.include_router(drug_info_router, prefix="/drug_info", tags=["Drug Information"])
app.include_router(ai_router, prefix="/ai", tags=["AI Services"])
app.include_router(ocr_router, prefix="/ocr", tags=["OCR Services"])
app.include_router(ner_router, prefix="/ner", tags=["NER Services"])
app.include_router(alt_router, prefix="/alternatives", tags=["Alternative Medications"])
app.include_router(prediction_router, prefix="/prediction", tags=["Disease Prediction"])


@app.on_event("startup")
async def startup_event():
    logger.info("Medify Backend Starting")


@app.get("/")
def home():
    return {"Message": "Welcome to Medify. Use /docs for API documentation."}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
