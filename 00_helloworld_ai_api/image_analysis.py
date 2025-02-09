import google.generativeai as genai
import PIL.Image
from config import configure_gemini


configure_gemini()
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_image(image_path, prompt):
    """Analyze an image using Gemini API with a user-provided prompt."""
    img = PIL.Image.open(image_path)
    response = model.generate_content([prompt, img])
    return response.text

if __name__ == "__main__":
    image_path = input("Enter the image file path: ")  
    prompt = input("Enter your prompt for image analysis: ")  
    
    response = analyze_image(image_path, prompt)
    print("\nGemini Image Analysis:\n", response)
