import google.oauth2.service_account
from google.cloud import vision


def get_gcp_vision_client(credentials_info: dict):
    """
    Initializes the Google Cloud Vision client from credentials info.
    """
    try:
        credentials = google.oauth2.service_account.Credentials.from_service_account_info(credentials_info)
        client = vision.ImageAnnotatorClient(credentials=credentials)
        return client
    except Exception as e:
        raise ConnectionError(f"Failed to create Google Cloud Vision client: {e}")


def extract_text_from_bytes(client, image_bytes: bytes) -> str:
    """
    Uses the provided client to extract text from image bytes.
    """
    if not client:
        raise ValueError("Google Cloud Vision Client is not initialized.")
    try:
        image = vision.Image(content=image_bytes)
        response = client.document_text_detection(image=image)

        if response.error.message:
            raise Exception(f"Google Cloud Vision API Error: {response.error.message}")

        return response.full_text_annotation.text
    except Exception as e:
        raise RuntimeError(f"An error occurred during OCR processing: {e}")
