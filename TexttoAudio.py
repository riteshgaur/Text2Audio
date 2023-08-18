
#Author: Ritesh Gaur
#Aug, 2023
#https://www.linkedin.com/in/riteshgaur/

import pyttsx3
import time



from gtts import gTTS
import os

texts= [
   "Our team utilizing RunwayML's Gen-2 is a AI system that can generate novel videos with text, images or video clips."
]
for i, text in enumerate(texts):
    tts = gTTS(text)
    filename = f"output_{i}.mp3"
    tts.save(filename)

# Pause for 1 second between each line
    time.sleep(1)

##################################