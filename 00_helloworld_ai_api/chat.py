import google.generativeai as genai
from config import configure_gemini


configure_gemini()
model = genai.GenerativeModel('gemini-1.5-flash')

def chat():
    """Chat with Gemini using memory"""
    chat_session = model.start_chat(history=[])
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended.")
            break
        response = chat_session.send_message(user_input)
        print("Gemini:", response.text)

if __name__ == "__main__":
    chat()
