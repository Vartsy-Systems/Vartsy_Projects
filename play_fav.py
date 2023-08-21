import webbrowser
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
user_greetings = input("User: ")

vartsy_response = "Hello Sir, How may I help you?"
print(vartsy_response)

engine.say(vartsy_response)
engine.runAndWait()
# Message to be spoken
user_command = input("User: ")
if user_command.lower() == "Open Vartsy youtube channel".lower():
    message = "Okay Sir."
    print(message)
    engine.say(message)
    print(" ")
    launcher_msg = "Opening Vartsy System Channel"
    print(launcher_msg)
    engine.say(launcher_msg)
    engine.runAndWait()

    # URL for YouTube
    youtube_url = "https://www.youtube.com/channel/UC1s4X24AeZKWR-T3dm2ENCg"

    # Open YouTube in the default web browser
    webbrowser.open(youtube_url)
