import time
import logging
from gemini_utils import generate_text


logging.basicConfig(
    filename="gemini.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if __name__ == "__main__":
    try:
        logging.info("Application started.")
        
        prompt = input("Enter a prompt: ").strip()
        response = generate_text(prompt)

        print("\nGemini Response:\n", response)
        logging.info(f"User prompt: {prompt}")
        logging.info(f"AI Response: {response}")

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        logging.warning("User interrupted the process.")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        logging.error(f"Unexpected error: {str(e)}")

    finally:
        time.sleep(2)  
        logging.info("Application finished.")
