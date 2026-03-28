# features/ocr.py

from google.cloud import vision
import google.auth


def get_gcp_vision_client(credentials_info: dict):
    """
    Initializes the Google Cloud Vision client from credentials info.
    """
    try:
        credentials = google.oauth2.service_account.Credentials.from_service_account_info(credentials_info)  # type: ignore
        client = vision.ImageAnnotatorClient(credentials=credentials)
        return client
    except Exception as e:
        # Let the caller handle the error display
        raise ConnectionError(f"Failed to create Google Cloud Vision client: {e}")


def extract_text_from_bytes(client, image_bytes: bytes) -> str:
    """
    Uses the provided client to extract text from image bytes.
    This function is now completely independent of Streamlit.
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
        # Re-raise the exception so the UI can catch it and display a message
        raise RuntimeError(f"An error occurred during OCR processing: {e}")
