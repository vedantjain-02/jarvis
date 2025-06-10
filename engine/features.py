import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

# playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query= query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("opening "+query)
        os.system('start '+query)
    else:
        speak("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing "+search_term+" on youtube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    # define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # if a match is found, return the extracted song name; otherwise return none
    return match.group(1) if match else None