**WhatsApp Voice Assistant**





This Python project is a voice-activated assistant that allows you to send WhatsApp messages using voice commands. It uses the following technologies:






Speech Recognition: Google Speech Recognition API for converting voice to text.





Text-to-Speech (TTS): pyttsx3 for voice responses.






WhatsApp Messaging: pywhatkit to schedule WhatsApp messages.





**Features**
        Send WhatsApp messages by speaking the contact's name and the message.
        Switch between English and Urdu voice commands.
        Case-insensitive contact recognition.
        Retry mechanism for improved voice recognition.
        Prerequisites



        
**Ensure you have the following installed:**





Python 3.x






pip (Python Package Installer)






**Required Libraries**






Install the necessary libraries using the following command:






      pip install SpeechRecognition pyttsx3 pywhatkit pyaudio





      
Notes:





On some systems (like Windows), you may need to separately install PyAudio. For Windows, download the appropriate .whl file from this link and install it using:






        pip install <path-to-downloaded-wheel-file>





        
Ensure your microphone is connected and working.





Configuration






Contacts Dictionary






Add your contacts in the contacts dictionary in a lowercase format:

          contacts = {
              "hamza": "+923188361229",
              
            }


Note: Contact names are stored in lowercase for case insensitivity. Ensure you say the name clearly during voice commands.




Usage



Clone the Repository:





          git clone <repository-url>
          cd <repository-folder>





          
Run the Assistant:






        python your_assistant_file_name.py



Voice Commands:



To send a WhatsApp message, say:

"WhatsApp"



The assistant will ask for the contact's name and the message.




To switch to Urdu, say:



"Switch to Urdu"




To switch to English, say:




"Switch to English"




To exit the assistant, say:



"Exit" or "Stop"




**Example Conversation:**

          Assistant: Hello, I am your assistant. How can I help you today?
          You: WhatsApp
          Assistant: Who would you like to message?
          You: Hamza
          Assistant: What should I say?
          You: I will play today
          Assistant: Sending message to +923188361229
          Assistant: Message scheduled on WhatsApp.
          Troubleshooting:
          If the assistant does not recognize your voice clearly, ensure:
          Your microphone is properly configured and has no background noise.
          You speak clearly and close to the microphone.
          Adjust energy_threshold in the listen() function if needed:






recognizer.energy_threshold = 300  # Adjust value if necessary




**Dependencies Used:**





SpeechRecognition: For converting voice to text.




Pyttsx3: For text-to-speech output.




PyWhatKit: For scheduling WhatsApp messages.




PyAudio: For capturing audio input.






**Contributing**





Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or create a pull request.





Author




Muhammad Hamza




Contact




Feel free to reach out for any questions or support.






**Disclaimer**





This project schedules messages using pywhatkit, which opens WhatsApp Web. You need to have an active internet connection, and WhatsApp Web should be linked to your phone.
