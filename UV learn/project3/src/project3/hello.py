from litellm import completion
import os



os.environ['GEMINI_API_KEY'] = "AIzaSyC7E9nn3PlMguT5NiLgNjefi3Fm0icOc2E"

def call_gemini():
    response = completion(
    model="gemini/gemini-2.0-flash",
    messages=[{"role": "user", "content": "hi how are you?"}]
)
    
    print(response['choices'][0]['message']['content'])