**Smart Home Voice-Controlled AI Agent Documentatio**






**1. Overview**






The Smart Home Voice-Controlled AI Agent is a Python-based program that continuously listens for voice commands. It accepts temperature values as voice input, interprets the spoken number to decide the corresponding device action (such as adjusting fan speed or turning on a heater), and provides audible feedback using text-to-speech. The agent runs continuously until you say “stop” to exit.






**2. Prerequisites**






Python: Version 3.6 or higher (download from https://www.python.org/downloads/).





Required Python Libraries:





speech_recognition – Captures and converts voice input to text.





pyttsx3 – Provides text-to-speech functionality.





pyaudio – Enables microphone access (installation may require platform-specific steps).






3. Installation Steps






Install Python (if not already installed).






Install the required libraries by opening your terminal or command prompt and running:


          pip install SpeechRecognition pyttsx3 pyaudio




          
Save the complete code (provided below in “The Complete Code” section) into a file named, for example, smart_home_agent.py.





**4. The Complete Code**






     
     import sys
     # Reconfigure stdout to UTF-8 to support emojis on Windows
     sys.stdout.reconfigure(encoding='utf-8')
     
     import speech_recognition as sr
     import pyttsx3
     
     class SmartHomeAgent:
     def __init__(self):
     self.device_status = "OFF"
     self.speaker = pyttsx3.init()
     
     def speak(self, text):
     """Convert text to speech and print the message."""
     print(f"[Agent] {text}")
     self.speaker.say(text)
     self.speaker.runAndWait()
     
     def perceive(self, temperature):
     """Decide the action based on the temperature value."""
     print(f"\n[Agent] Checking temperature: {temperature}°C")
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
     """Announce the device status by speaking it aloud and printing it."""
     self.speak(f"Device Status: {self.device_status}")
     
     def listen(self):
     """
     Capture voice input and process the command.
     Accepts either a temperature (number) or the word 'stop' to exit.
     """
     recognizer = sr.Recognizer()
     with sr.Microphone() as source:
     print("[Agent] Listening for command...")
     self.speak("Please say a temperature value or say stop to exit.")
     # Adjust for ambient noise to improve accuracy
     recognizer.adjust_for_ambient_noise(source, duration=1)
     try:
     audio = recognizer.listen(source, timeout=5)
     print("[Agent] Processing voice input...")
     try:
     # Use Google Speech Recognition first
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
     # Loop continuously until the user says "stop"
     while True:
     command = agent.listen()
     if command == "stop":
     agent.speak("Shutting down. Goodbye!")
     break
     elif command is not None:
     agent.perceive(command)



     
**5. How the Code Works**





Reconfiguring Output Encoding:






The script sets the standard output to UTF-8 to support Unicode characters (such as emojis) on Windows.






**Initialization:**




The SmartHomeAgent class is created with an initial device status set to “OFF” and a text-to-speech engine initialized using pyttsx3.






**Speaking Functionality:**




The speak() method prints messages to the console and converts text to audible speech.





**Decision Making (Perception):**





The perceive() method accepts a temperature value, determines the appropriate device status based on the temperature, and then calls the act() method.





**Acting on Decisions:**





The act() method announces the device status using the speak() method.




**Listening for Commands:**





The listen() method captures voice input via the microphone, processes the input using the speech_recognition library, and accepts either a temperature value or the word “stop” to exit the loop.







**Continuous Loop:**





The main block runs a continuous loop, allowing the agent to process multiple commands until “stop” is spoken.







**6. Running the Application**




Open your terminal or command prompt.




Navigate to the directory where smart_home_agent.py is saved.





Run the script by entering:





          nginx
          python smart_home_agent.py
          Follow the prompts:
          Speak a temperature value (e.g., "25") to get a response.
          Say “stop” to exit the program.




          
**7. Troubleshooting**






**Microphone Issues:**





Ensure your microphone is properly connected and set up. Check your system’s audio input settings.






**Speech Recognition Errors:**





Speak clearly in a quiet environment. If recognition fails, adjust the ambient noise duration in the code if needed.

**Unicode/Emoji Errors:**





If you experience display issues with emojis, ensure that the sys.stdout.reconfigure(encoding='utf-8') line is present at the beginning of the code. You may also remove emojis from the output strings if necessary.





**8. Future Enhancements**




Expand command recognition to support additional home automation tasks.





Integrate with real IoT devices for actual hardware control.





Improve error handling and add logging for a more robust application.






Develop a graphical user interface (GUI) to complement the voice commands.
