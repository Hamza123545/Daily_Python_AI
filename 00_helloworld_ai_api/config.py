import google.generativeai as genai
import absl.logging


absl.logging.set_verbosity("info")


API_KEY = "your-api-key"

def configure_gemini():
    genai.configure(api_key=API_KEY)
