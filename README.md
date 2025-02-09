G**oogle Gemini AI Integration - Setup Guide**





**📌 Project Structure**





**gemini_project/**



│── config.py
│── gemini_utils.py
│── main.py
│── requirements.txt



**1️⃣ Step 1: Install Dependencies**




First, install the required Python packages:





pip install google-generativeai absl-py
Create a requirements.txt file and add:





google-generativeai
absl-py




**To install dependencies later, run:**






pip install -r requirements.txt




        **2️⃣ Step 2: Create Configuration File**





        
Create a file named config.py to store API configuration:






import google.generativeai as genai




# Configure Gemini API



def configure_gemini():
    API_KEY = "your-api-key-here"
    genai.configure(api_key=API_KEY)
🛠 Replace "your-api-key-here" with your actual Google Gemini API key.






**3️⃣ Step 3: Create Utility File**






**Create gemini_utils.py to handle AI text generation:**




import google.generativeai as genai
import logging
from config import configure_gemini




# Configure logging




logging.basicConfig(filename="gemini.log", level=logging.INFO, 





                    format="%(asctime)s - %(levelname)s - %(message)s")



                    

# Initialize Gemini API




configure_gemini()




# Function to generate text using Gemini AI




def generate_text(prompt):
    try:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty!")

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        logging.info(f"User Prompt: {prompt}")
        logging.info(f"Gemini Response: {response.text}")
        
        return response.text

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return "An error occurred. Please try again!"





        
✅ Features:

Logs user prompts & AI responses
Handles empty input errors
Catches API failures







**4️⃣ Step 4: Create Main Script**
Create main.py to run the chatbot:








import time
from gemini_utils import generate_text

if __name__ == "__main__":
    try:
        while True:
            prompt = input("\nEnter a prompt (or type 'exit' to quit): ")
            if prompt.lower() == "exit":
                print("Goodbye!")
                break

            response = generate_text(prompt)
            print("\nGemini Response:\n", response)

            time.sleep(1)  # Small delay for smooth execution

    except KeyboardInterrupt:
        print("\nSession terminated by user.")





        
✅ Features:

Accepts user input
Calls Gemini AI for responses
Allows exiting via "exit" or Ctrl + C






**5️⃣ Step 5: Run the Application**








To start the chatbot, run:





python main.py
💡 Example:


Enter a prompt: What is AI?  
Gemini Response: AI (Artificial Intelligence) is a field of computer science






**6️⃣ Step 6: Debugging & Logs**





All logs are saved in gemini.log.
If any error occurs, check the log file.
