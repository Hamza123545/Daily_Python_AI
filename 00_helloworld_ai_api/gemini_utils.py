import google.generativeai as genai
import logging
from config import configure_gemini


logging.basicConfig(
    filename="gemini.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


configure_gemini()

def generate_text(prompt: str) -> str:
    """Generates text from Gemini AI based on the given prompt."""
    try:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            logging.info("Text generated successfully.")
            return response.text
        else:
            logging.warning("Received an empty response from Gemini AI.")
            return "No response received from the AI."

    except Exception as e:
        logging.error(f"Error in generate_text: {str(e)}")
        return f"An error occurred: {str(e)}"
