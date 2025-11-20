from voice.speech_to_text import listen
# from voice.text_to_speech import speak    # old pyttsx3 based TTS
from jarvis_voice import speak    # new elevenlabs based TTS
from vision import start_face_detection
# from object_detection import start_object_detection
# from object_detection import start_hand_gesture_detection
from weather import get_weather
from battery_status import get_battery_status
# from ai_chat import ask_chatgpt
from gemini_ai import ask_gemini



import os
import webbrowser
import datetime
# import pyjokes



speak("""allow me to introduce myself, I am Jarvis,  a virtual artificial intelligence, 
      and I'm here to assist you with a variety of tasks, as best I can, 24 hours a day,
      7 days a week, importing all preferences from home interface, systems are now fully operational""")

while True:
    command = listen().lower()

    if "jarvis" in command:
        speak("How can I help you? Sir. ") # ok tested on 30-07-2025

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Sir, the time is {time}")    # ok tested on 30-07-2025

    elif "open youtube" in command:
        speak("Sir,I Opening YouTube")
        webbrowser.open("https://www.youtube.com")   # ok tested on 30-07-2025

    elif "open notepad" in command:
        speak("Opening Notepad Sir")
        os.system("notepad.exe")     # ok tested on 30-07-2025

    elif "search" in command:
        speak("What should I search? Sir")
        search_query = listen().lower()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Here are the results for {search_query}")     # ok tested on 30-07-2025

    # elif "joke" in command:
    #     joke = pyjokes.get_joke()
    #     speak(joke)

    elif "open code" in command or "open vs code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")       # ok tested on 30-07-2025

    elif "open file explorer" in command:
        speak("Opening File Explorer")
        os.system("explorer")       # ok tested on 30-07-2025

    elif "open chrome" in command:
        speak("Opening Google Chrome")
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)    # ok tested on 30-07-2025

    
    
    elif "start face detection" in command or "vision mode" in command:
        speak("Activating JARVIS Vision. Starting face detection.")
        start_face_detection()    # ok tested on 30-07-2025

    elif "photo" in command:
        speak("Smile please, Sir")
        from vision import take_screenshot
        take_screenshot()       # ok tested on 30-07-2025

    # elif "object detection" in command:
    #     speak("Starting object detection mode.")
    #     start_object_detection()     
        
    # elif "gesture" in command:
    #     start_hand_gesture_detection()
        
    elif "weather" in command:
        weather_info = get_weather("Noida")  # or dynamically detect city later
        speak(weather_info)  # ok tested on 30-07-2025


    elif "battery" in command or "battery status" in command:
        speak(get_battery_status())   # ok tested on 30-07-2025


    elif "ai" in command or "question" in command:
        speak("What would you like to ask?")
        user_query = listen()

        if user_query:
            response = ask_gemini(user_query)
            print(f"AI Response: {response}")
            speak(response)
        else:
            speak("Sorry, I didn’t catch your question.")     # ok tested on 30-07-2025
            
            
            
# THE JARVIS WILL STOP IF I SAY EXIT OR STOP             
    elif "exit" in command or "stop" in command:
            speak("Goodbye Sir. See you soon.")
            break