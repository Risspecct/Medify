from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.ocr_processor import get_gcp_vision_client, extract_text_from_bytes
import os
import json

router = APIRouter()

# Initialize the client globally within the router scope
# It pulls the credentials from your environment variable
try:
    gcp_json_str = os.getenv("GCP_SERVICE_ACCOUNT_JSON")
    if not gcp_json_str:
        raise ValueError("GCP_SERVICE_ACCOUNT_JSON not found in environment.")

    credentials_info = json.loads(gcp_json_str)
    vision_client = get_gcp_vision_client(credentials_info)
except Exception as e:
    # We don't want the whole app to crash if OCR isn't configured,
    # but we should log it.
    print(f"OCR Client Initialization Warning: {e}")
    vision_client = None


@router.post("/extract")
async def ocr_extract(file: UploadFile = File(...)):
    """
    Endpoint to upload an image and receive extracted text.
    """
    if not vision_client:
        raise HTTPException(status_code=500, detail="OCR Service is not configured.")

    try:
        # Read the uploaded file content
        image_bytes = await file.read()

        # Call the utility function
        extracted_text = extract_text_from_bytes(vision_client, image_bytes)

        return {
            "filename": file.filename,
            "extracted_text": extracted_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
