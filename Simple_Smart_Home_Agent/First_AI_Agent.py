import sys
sys.stdout.reconfigure(encoding='utf-8')

import speech_recognition as sr
import pyttsx3

class SmartHomeAgent:
    def __init__(self):
        self.device_status = "OFF"
        self.speaker = pyttsx3.init()

    def speak(self, text):
        """Convert text to speech and print the message."""
        print(f"[Hamza's Agent] {text}")
        self.speaker.say(text)
        self.speaker.runAndWait()

    def perceive(self, temperature):
        """Decide action based on the temperature value."""
        print(f"\n[Hamza's Agent] Checking temperature: {temperature}°C")
        if temperature < 10:
            self.device_status = "Heater ON 🔥"
        elif 10 <= temperature <= 20:
            self.device_status = "Fan ON (Low Speed) 🌬"
        elif 21 <= temperature <= 30:
            self.device_status = "Fan ON (Medium Speed) 🌬🌬"
        elif temperature > 30:
            self.device_status = "Fan ON (High Speed) 🌬🌬🌬"
        else:
            self.device_status = "OFF ❌"
        self.act()

    def act(self):
        """Announce the action taken."""
        self.speak(f"Device Status: {self.device_status}")

    def listen(self):
        """
        Capture voice input and process the command.
        Accepts either a temperature (number) or the word "stop" to exit.
        """
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("[Hamza's Agent] Listening for command...")
            self.speak("Please say a temperature value or say stop to exit.")
        
            recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = recognizer.listen(source, timeout=5)
                print("[Hamza's Agent] Processing voice input...")
                try:
                 
                    command_text = recognizer.recognize_google(audio)
                except sr.RequestError:
                  
                    self.speak("Google speech recognition is unavailable. Switching to offline mode.")
                    command_text = recognizer.recognize_sphinx(audio)
                
                print(f"[User] You said: {command_text}")

               
                if command_text.lower().strip() == "stop":
                    return "stop"
                
            
                try:
                    temperature = int(command_text)
                    return temperature
                except ValueError:
                    self.speak("I didn't catch a valid number. Please try again.")
                    return None

            except sr.UnknownValueError:
                self.speak("Sorry, I didn't understand. Please try again.")
                return None
            except sr.WaitTimeoutError:
                self.speak("You took too long. Please try again.")
                return None

if __name__ == "__main__":
    agent = SmartHomeAgent()
 
    while True:
        command = agent.listen()
        if command == "stop":
            agent.speak("Shutting down. Goodbye!")
            break
        elif command is not None:
            agent.perceive(command)

