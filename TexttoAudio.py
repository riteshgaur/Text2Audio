
#Author: Ritesh Gaur
#Aug, 2023
#https://www.linkedin.com/in/riteshgaur/

import pyttsx3
import time



from gtts import gTTS
import os

texts= [
   "Hello! This is what I will say in the audio file."
]
for i, text in enumerate(texts):
    tts = gTTS(text)
    filename = f"output_{i}.mp3"
    tts.save(filename)

# Pause for 1 second between each line
    time.sleep(1)

##################################
