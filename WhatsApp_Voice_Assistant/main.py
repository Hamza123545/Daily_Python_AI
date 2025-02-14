import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import time
import google.generativeai as genai
import os

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

# Configure Gemini API
genai.configure(api_key="Ayour Api")  #
model = genai.GenerativeModel('gemini-pro')

# Contacts dictionary
contacts = {
    "hamza": "+923188361229",
    # Add more contacts here
}

# Function to speak text
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen(language="en-US", retries=3):
    for _ in range(retries):
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.energy_threshold = 300
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language=language)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand. Please try again.")
            speak("Sorry, I did not understand. Please try again.")
        except sr.RequestError:
            print("Sorry, the service is down. Please try again later.")
            speak("Sorry, the service is down. Please try again later.")
    return None

# Function to process user commands
def process_command(command):
    if "whatsapp" in command:
        handle_whatsapp_command()
    elif "switch to urdu" in command:
        speak("Switching to Urdu.")
        return "ur-PK"
    elif "switch to english" in command:
        speak("Switching to English.")
        return "en-US"
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        handle_gemini_query(command)
    return None

# Function to handle WhatsApp commands
def handle_whatsapp_command():
    speak("Who would you like to message? Please say the names separated by 'and'.")
    names_input = listen()
    if names_input:
        names = [name.strip() for name in names_input.split("and")]
        speak("What should I say?")
        message = listen()
        if message:
            contacts_list = get_contacts(names)
            if contacts_list:
                send_whatsapp_messages(contacts_list, message)
            else:
                speak("Sorry, I don't have those contacts.")
        else:
            speak("I didn't catch the message.")
    else:
        speak("I didn't catch the names.")

# Function to handle Gemini queries
def handle_gemini_query(query):
    try:
        response = model.generate_content(query)
        speak("Here's what I found:")
        speak(response.text)
        speak("Would you like to send this to someone on WhatsApp?")
        confirmation = listen()
        if confirmation and "yes" in confirmation:
            handle_whatsapp_command()
    except Exception as e:
        print(f"Error generating response: {e}")
        speak("Sorry, I couldn't generate a response. Please try again.")

# Function to send WhatsApp messages
def send_whatsapp_messages(contacts_list, message):
    for contact in contacts_list:
        speak(f"Sending message to {contact}")
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute + 2
        kit.sendwhatmsg(contact, message, hour, minute)
        time.sleep(2)
    speak("Messages scheduled on WhatsApp.")

# Function to get contacts
def get_contacts(names):
    valid_contacts = []
    for name in names:
        name = name.lower()
        if name in contacts:
            valid_contacts.append(contacts[name])
        else:
            speak(f"Sorry, I don't have a contact for {name}.")
    return valid_contacts

# Main function
if __name__ == "__main__":
    speak("Hello, I am your advanced assistant. How can I help you today?")
    current_language = "en-US"
    while True:
        command = listen(language=current_language)
        if command:
            new_language = process_command(command)
            if new_language:
                current_language = new_language
        else:
            speak("I didn't catch that. Could you please repeat?")
