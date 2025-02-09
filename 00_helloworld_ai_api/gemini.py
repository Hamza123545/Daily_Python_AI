import google.generativeai as genai
from config import configure_gemini


configure_gemini()

def generate_text(prompt: str) -> str:
    """
    Generates text using Google's Gemini API.
    
    Args:
        prompt (str): The input prompt for the AI.

    Returns:
        str: The generated text response.
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    

    if response and response.text:
        return response.text
    else:
        return "No response from Gemini API."
