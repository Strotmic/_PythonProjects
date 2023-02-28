import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 250)
engine.setProperty('voice', voices[3].id)
engine.say('Hello')

for voice in voices:
    print(voice, voice.id)
engine.runAndWait()
