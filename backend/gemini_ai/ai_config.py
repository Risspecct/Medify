from dotenv import load_dotenv
import os

# Minimal Gemini wrapper using google.generativeai
try:
    import google.generativeai as genai
except Exception:
    raise RuntimeError("google-generative-ai package not found. Install it to use AI features.")

# Load env vars
load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")

if genai is None:
    raise RuntimeError("google-generative-ai package not installed. Install the client to use AI features.")
if not GENAI_API_KEY:
    raise RuntimeError("GENAI_API_KEY is not set. Please set it in your environment or .env file.")

# Configure client
genai.configure(api_key=GENAI_API_KEY)


class GeminiModel:
    def __init__(self, model_id: str = "gemini-2.5-flash"):
        # Hard‑coded default model
        self.model = genai.GenerativeModel(model_id)

    def generate_text(self, prompt: str) -> str:
        resp = self.model.generate_content(prompt)
        return getattr(resp, "text", str(resp))


# Expose a single instance
gemini_model = GeminiModel()
