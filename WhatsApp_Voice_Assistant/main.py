import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import time


recognizer = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


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


def process_command(command):
    if "whatsapp" in command:
        speak("Who would you like to message? Please say the names separated by 'and'.")
        names_input = listen()
        if names_input:
            names = [name.strip() for name in names_input.split("and")]
            speak("What should I say?")
            message = listen()
            if message:
                contacts = get_contacts(names)
                if contacts:
                    send_whatsapp_messages(contacts, message)
                else:
                    speak("Sorry, I don't have those contacts.")
            else:
                speak("I didn't catch the message.")
        else:
            speak("I didn't catch the names.")
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
        speak("Sorry, I can't do that yet.")
    return None


def send_whatsapp_messages(contacts, message):
    for contact in contacts:
        speak(f"Sending message to {contact}")
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute + 2 
        kit.sendwhatmsg(contact, message, hour, minute)
        time.sleep(2)  
    speak("Messages scheduled on WhatsApp.")


contacts = {
    "hamza": "+923188361229",
    
}


def get_contacts(names):
    valid_contacts = []
    for name in names:
        name = name.lower()  
        if name in contacts:
            valid_contacts.append(contacts[name])
        else:
            speak(f"Sorry, I don't have a contact for {name}.")
    return valid_contacts


if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you today?")
    current_language = "en-US"
    while True:
        command = listen(language=current_language)
        if command:
            new_language = process_command(command)
            if new_language:
                current_language = new_language
        else:
            speak("I didn't catch that. Could you please repeat?")