# Import the gTTS module
from gtts import gTTS
 
# This the os module so we can play the MP3 file generated
import os
 
# Generate the audio using the gTTS engine. We are passing the message and the language
audio = gTTS(text='I love Python for text to speech, and you?', lang='en')
 
# Save the audio in MP3 format
audio.save("message.mp3")
 
# Play the MP3 file
os.system("afplay message.mp3")