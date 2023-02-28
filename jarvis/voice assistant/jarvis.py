import sys
import threading
from pyaudio import paPrimingOutput
from pynput.keyboard import Key, Controller
from urllib import request
sys.path.append("C:/Users/Gebruiker/AppData/Local/Programs/Python/Python39/Lib/site-packages")
from os import close
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import pyautogui
import psutil 
import pyjokes
import requests
import cv2
from newsapi import NewsApiClient
import pycountry
import multiprocessing
import keyboard as kyb
import time


#import pygoogle


#import pre trained data on face frontals from opencv
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
keyboard = Controller()
def __init__(self):
    self.voorlopig=""

engine = pyttsx3.init()
engine.say("")
engine.runAndWait()


voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
engine.setProperty('voice', voice_id)  
for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)

def say(audio):
    threading.Thread(target=say(audio)).start()
    while True:
        if kyb.is_pressed('a'):
            break
        if engine.isBusy == False:
            kyb.press('q')
       
def speak(self,audio):
    self.voorlopig = str(audio)
    engine.say(audio)
    engine.runAndWait()
 
    
def repeat(self):
    speak(self.voorlopig)
    
def time():
    #Time = datetime.datetime.now().strftime("%I:%M:%S")
    hours = int(datetime.datetime.now().hour)
    ''''if hours==15|3:
        hours="three"
    elif hours==1|13:
        hours="one"
    elif hours==0:
        hours="zero"
    elif hours==2|14:
        hours="two"
    elif hours==16|4:
        hours="four"
    elif hours==5|17:
        hours="five"
    elif hours==6|18:
        hours="six"
    elif hours==7|19:
        hours="seven"
    elif hours==8|20:
        hours="eight"
    elif hours==9|21:
        hours="nine"
    elif hours==10|22:
        hours="ten"
    elif hours==11|23:
        hours="eleven"
    elif hours==12:
        hours="twelve"'''
    minutes= int(datetime.datetime.now().minute)
    seconds= int(datetime.datetime.now().second)
    speak("The current time is " + str(hours) + " hours "+ str(minutes)+ " minutes" + str(seconds) + " seconds")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    if month ==1:
        month="january"
    if month ==2:
        month="februari"
    if month ==3:
        month="march"
    if month ==4:
        month="april"
    if month ==5:
        month="may"
    if month ==6:
        month="june"
    if month ==7:
        month="july"
    if month ==8:
        month="august"
    if month ==9:
        month="september"
    if month ==10:
        month="october"
    if month ==11:
        month="november"
    if month ==12:
        month="december"   
    day = int(datetime.datetime.now().day)
    speak("The current date is" + str(day) + month + str(year))

def wishme():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning sir! Hope you slept well Tim")
    if hour >=12 and hour<18:
        speak("Good afternoon sir! Hope you having a good day Tim")
    if hour >=18 and hour<24:
        speak("Good evening sir! Hope you had a good day Tim")
    if hour >=24 and hour<6:
        speak("Good night, shouldn't you be asleep sir?")
    #speak("Welcome back Tim!")
    time()
    date()
    weather2()
    speak("I'm at your service sir, give me a yell when i can help")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        #r.pause.threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        return "None"

    return query
    quit



def email(to,content):
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('',"")
    server.sendmail('tim.blz042@gmail.com', to, content )
    server.close

    """elif 'send email' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "tim.bleuze@gmail.com"
                #speak("to who shal i send this mail")
                #to = takeCommand()
                speak("are you sure you want to send the mail to" + to)
                print(to)
                answer = takeCommand()
                if answer =="yes": 
                    email(to,content)
                    speak("email has been sent to" + to)
                if answer =="no":
                    speak("The email hasnt been send")
            except Exception as e:
                print(e)
                speak("uanble to send the email")"""
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Gebruiker/Desktop/programeren/Python/jarvis/ss/ss.png")

def cpu():
    usage = str(psutil.cpu_percent()) 
    speak("The usage is" + usage) 

def jokes():
    speak(pyjokes.get_joke())   

def weather():
    user_api = "2461edc6fffc7f9270d4673d769aa3ad"
    speak("Where do you want to check the weather")
    city = takeCommand()
    speak("")
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city + "&appid="+ user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    #decoding
    if api_data['cod'] == '404':
        speak("Invalid city, Please check again")
        pass
    else:
        temp_city = ((api_data['main']['temp'])-273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        wind_drt = api_data['wind']['deg']

    if wind_drt >=337.5 and wind_drt<= 360: 
        wind_drt = "north"
    elif wind_drt >=0 and wind_drt<=22.5:
        wind_drt = "north"
    elif wind_drt >=22.5 and wind_drt<=67.5:
        wind_drt = "north-east"
    elif wind_drt >=67.5 and wind_drt<=112.5:
        wind_drt = "east"
    elif wind_drt >=112.5 and wind_drt<=157.5:
        wind_drt = "south-east"
    elif wind_drt >=157.5 and wind_drt<=202.5:
        wind_drt = "south"
    elif wind_drt >=202.5 and wind_drt<=247.5:
        wind_drt = "south-west"
    elif wind_drt >=247.5 and wind_drt<=292.5:
        wind_drt = "west"
    elif wind_drt >=292.5 and wind_drt<=337.5:
        wind_drt = "north-west"

    temp_city = "{:.2f}".format(temp_city)
    speak("These are the weather stats for"+ city)
    speak("It is currently"+ str(temp_city) + "Degrees Celcius. It is" + str(weather_desc) + "The humidity is" + str(hmdt) + "the wind speed is" + str(wind_spd) + "kilometers per hour" + " and the direction is " + str(wind_drt))

def weather2():
    user_api = "2461edc6fffc7f9270d4673d769aa3ad"
    city = "Zwevegem"
    speak("")
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city + "&appid="+ user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    #decoding
    if api_data['cod'] == '404':
        speak("Invalid city, Please check again")
    else:
        temp_city = ((api_data['main']['temp'])-273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        wind_drt = api_data['wind']['deg']

    if wind_drt >=337.5 and wind_drt<= 360:
        wind_drt = "north"
    elif wind_drt >=0 and wind_drt<=22.5:
        wind_drt = "north"
    elif wind_drt >=22.5 and wind_drt<=67.5:
        wind_drt = "north-east"
    elif wind_drt >=67.5 and wind_drt<=112.5:
        wind_drt = "east"
    elif wind_drt >=112.5 and wind_drt<=157.5:
        wind_drt = "south-east"
    elif wind_drt >=157.5 and wind_drt<=202.5:
        wind_drt = "south"
    elif wind_drt >=202.5 and wind_drt<=247.5:
        wind_drt = "south-west"
    elif wind_drt >=247.5 and wind_drt<=292.5:
        wind_drt = "west"
    elif wind_drt >=292.5 and wind_drt<=337.5:
        wind_drt = "north-west"

    temp_city = "{:.2f}".format(temp_city)
    speak("These are the weather stats for"+ city)
    speak("It is currently"+ str(temp_city) + "Degrees Celcius It is " + str(weather_desc) + " The humidity is " + str(hmdt) + " the wind speed is " + str(wind_spd) + " kilometers per hour " + " and the direction is " + str(wind_drt) )
def volume():
    volume = engine.getProperty('volume')
    print(volume)
    speak("what does the new volume need to be")
    answer = takeCommand()
    if answer=="one":
        engine.setProperty("volume",0.1)
    if answer=="two":
        engine.setProperty("volume",0.2)
    if answer=="three":
        engine.setProperty("volume",0.1)
    if  answer=="four":
        engine.setProperty("volume",0.4)
    if answer=="five":
        engine.setProperty("volume",0.5)
    if answer=="six":
        engine.setProperty("volume",0.6)
    if answer=="seven":
        engine.setProperty("volume",0.7)
    if answer=="eight":
        engine.setProperty("volume",0.8)
    if answer=="nine":
        engine.setProperty("volume",0.9)
    if answer=="ten":
        engine.setProperty("volume",1.0)
    if answer=="max":
        engine.setProperty("volume",1.0)
    
    speak("okay, the volume is now" + str(engine.getProperty("volume")))

def camera():
    webcam = cv2.VideoCapture(1)
    time = 0
    #loop zodat alle frames gedaan worden
    while True:

        #read the current frame
        successful_frame_read, frame = webcam.read()

        #convert to grayt scale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        #detect faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

        #draw rectangles arround faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x,  y ), (x + w ,y+h), (0,255,0),4 )
        #print(face_coordinates)

        #als er meer dan een gezicht gescanned word zegt de python hallo
        
        cv2.imshow("Face Regocnition" , frame)
        key = cv2.waitKey(1) # elke ms 
        time +=1
        if len(face_coordinates) >1 and time==50:
            speak("I see you're not alone sir, you two have fun, but i'm still here to assist")
        elif len(face_coordinates) ==1 and time==50:
            speak("I see you're alone sir, but i'm here to assist")

        #force stop when pressed button
        print(time)
        if  time==50:
            cv2.destroyAllWindows()
            break
        #release the webcam

def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "961eecc3a85345079f579241ceb5b5d9"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
		
		# printing all trending news
		print(i + 1, results[i])

	#to read the news out loud for us
	speak(results)
			

# hier staan alle voice commands

if __name__ == "__main__":

    camera()
    wishme()
    speak("Going in to standby")
    on=1
    
    
    while True:  
        print("listening")
        query = takeCommand().lower()
        if  "out of standby" in query:
            on = 1
            speak("Welcome back sir, i'm at your service")
        elif "hey jarvis" in query:
            on = 1
            speak("Welcome back sir, i'm at your service")
        while on==1:
            query = takeCommand().lower()
#BASIC COMMANDS

            if "time" in query:
                time()
            elif "how late is it" in query:
                time()
            elif "date" in query:
                date()
            elif "what day" in query:
                date()
            
            elif "take a screenshot" in query:
                screenshot()
                speak("I took a screenshot sir")
            elif "go in standby" in query:
                speak("Going in standby")
                on=0
            elif "go in to standby" in query:
                speak("Going in standby")
                on=0
            elif "tell a joke" in query:
                jokes()
            elif "tell me a joke" in query:
                jokes()
            elif "change volume" in query:
                volume()
            elif "tell me the news" in query:
                NewsFromBBC()
            elif "the news" in query:
                NewsFromBBC()
            elif 'shut up' in query:
                speak("okay sir i will shut up")
                on=0
            elif 'repeat' in query:
                repeat()
            elif 'say again' in query:
                repeat()
            elif 'open trades' in query:
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

                wb.get(chromepath).open_new_tab(search + '.com')
                
#LOOK UP COMMANDS
            elif "search on google" in query:
                speak("What should i look up?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab("https://www.kucoin.com/assets")
                wb.get(chromepath).open_new_tab("https://trade.kucoin.com/trade/QRDO-USDT")
                wb.get(chromepath).open_new_tab("https://ftx.com/markets")
                #wb.get(chromepath).open_new_tab("https://www.kucoin.com/assets")
                continue
                   
            elif "open google" in query:
                speak("What should i look up?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search + '.com')
                continue
            elif  "lookup on google" in query:
                speak("What should i look up?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search + '.com')
                continue
            elif "wikipedia" in query:
                speak("searching")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(query)
                print(result)
                speak(result)
            elif 'open disney' in query:
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = "https://www.disneyplus.com/nl-nl/home"
                wb.get(chromepath).open_new_tab(search)
                continue
            elif 'open netflix' in query:
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = "https://www.netflix.com/browse"
                wb.get(chromepath).open_new_tab(search) 
                continue
            
            elif "tell me everything you know about" in query:
                speak("searching")
                query = query.replace("tell me everything you know about","")
                try: 
                    result = wikipedia.summary(query)
                    print(query)
                    print(result)
                    chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                    search = "https://en.wikipedia.org/wiki/"+ query
                    wb.get(chromepath).open_new_tab(search) 
                    speak(result)   
                    continue                         
                except Exception as e:
                    print(e)
            elif "close google" in query:
                os.system("taskkill /im chrome.exe /f")
                
                    
#HIER STAAN ALLE COMMANDS OM DINGEN TE OPENEN
            elif 'play songs' in query:
                songs_dir = 'C:/Users/Gebruiker/AppData/Roaming/Spotify/Spotify.exe'
                os.startfile(songs_dir)
                os.system(songs_dir)

                """songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))"""
            elif 'open twitch' in query:
                songs_dir = 'C:/Windows.old/Users/Gebruiker/AppData/Roaming/Twitch/Bin/Twitch.exe'
                os.startfile(songs_dir)
                os.system(songs_dir)
        
            elif 'open discord' in query:
                songs_dir = "C:\\Users\\Gebruiker\\AppData\\Local\\Discord\\app-1.0.9003\\discord.exe" 
                os.startfile(songs_dir)
                os.system(songs_dir)
                continue
            elif 'open cmd' in query:
                subprocess.call('C:/Users/Gebruiker/Music/jarvis/cmd.exe')
    
            elif 'open shell' in query:
                subprocess.call('C:/Users/Gebruiker/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Windows PowerShell/powershell.exe')

            
#PC COMMANDS
            elif "cpu usage" in query:
                cpu()     
            elif "processor usage" in query:
                cpu()      
            elif 'you can shut down' in query:
                os.system("shutdown /s /t 1")
            
#remember dfunction
            elif 'remember that' in query:
                speak("What should i remember sir?")
                data = takeCommand()
                speak("you sure you want to remember " + data)
                answer = takeCommand()
                if answer=="yes":
                    remember = open("data.txt","w")
                    remember.write(data)
                    remember.close()
                    speak("i saved data")
                else:
                    speak("i will not save it")
            elif 'write something down for me' in query:
                speak("What should i remember sir?")
                data = takeCommand()
                speak("you sure you want to remember " + data)
                answer = takeCommand()
                if answer=="yes":
                    remember = open("data.txt","w")
                    remember.write(data)
                    remember.close()
                    speak("i saved data")
                else:
                    speak("i will not save it")
            elif "do you know anything" in query:
                remember =open('data.txt' , 'r')   
                speak("you said me to remember that" + remember.read())
            
            elif "anything important today" in query:
                remember =open('data.txt' , 'r')   
                speak("you said me to remember that" + remember.read())
            elif "have a thing to do today" in query:
                remember =open('data.txt' , 'r')   
                speak("you said me to remember that" + remember.read())
            elif "appointment" in query:
                remember =open('data.txt' , 'r')   
                speak("you said me to remember that" + remember.read())
            elif "clear the data" in query:
                remember = open("data.txt","r+")
                remember.truncate(0)
                speak("the data file has been cleared sir")
                speak(remember.read())
            elif "clear data" in query:
                remember = open("data.txt","r+")
                remember.truncate(0)
                speak("the data file has been cleared sir")
                speak(remember.read())
#weather forecast
            elif "what's the weather" in query:
                weather()
            elif "tell me the weather" in query:
                weather()
            elif "how is the weather in my town" in query:
                weather2()
            elif "what's the weather like in my city" in query:
                weather2()
            elif "what's the weather here" in query:
                weather2()
            elif "weather here" in query:
                weather2()
#alle keyboard commands
            elif 'press windows' in query:
                keyboard.press(Key.cmd)
                keyboard.release(Key.cmd)
            elif 'close program' in query:
                keyboard.press(Key.alt)
                keyboard.press(Key.f4)
                keyboard.release(Key.alt)
                keyboard.release(Key.f4)
            elif 'open new desktop' in query:
                keyboard.press(Key.cmd)
                keyboard.press(Key.ctrl)
                keyboard.press(Key.right)
                keyboard.release(Key.cmd)
                keyboard.release(Key.ctrl)
                keyboard.release(Key.right)

            elif 'open new screen' in query:
                keyboard.press(Key.cmd)
                keyboard.press(Key.ctrl)
                keyboard.press(Key.right)
                keyboard.release(Key.cmd)
                keyboard.release(Key.ctrl)
                keyboard.release(Key.right)
            elif 'new screen' in query:
                keyboard.press(Key.cmd)
                keyboard.press(Key.ctrl)
                keyboard.press(Key.right)
                keyboard.release(Key.cmd)
                keyboard.release(Key.ctrl)
                keyboard.release(Key.right)
            elif 'second screen' in query:
                keyboard.press(Key.cmd)
                keyboard.press(Key.ctrl)
                keyboard.press(Key.right)
                keyboard.release(Key.cmd)
                keyboard.release(Key.ctrl)
                keyboard.release(Key.right)
            elif 'go back' in query:
                keyboard.press(Key.cmd)
                keyboard.press(Key.ctrl)
                keyboard.press(Key.left)
                keyboard.release(Key.cmd)
                keyboard.release(Key.ctrl)
                keyboard.release(Key.left)
            elif 'first screen ' in query:
                keyboard.press(Key.cmd)
                keyboard.press(Key.ctrl)
                keyboard.press(Key.left)
                keyboard.release(Key.cmd)
                keyboard.release(Key.ctrl)
                keyboard.release(Key.left)
            elif 'mute discord' in query:
                keyboard.press(Key.end)
                keyboard.release(Key.end)
            elif 'unmute discord' in query:
                keyboard.press(Key.end)
                keyboard.release(Key.end)
#standard responses
            elif "that was a good one" in query:
                speak("Thank you sir i have been training my whole life for this")
            elif "that's a good one" in query:
                speak("Thank you sir i have been training my whole life for this")
            elif "that was funny" in query:
                speak("Thank you sir i'm glad you liked it")
            elif "good one jarvis" in query:
                speak("Thank you sir i have been training my whole life for this")
            elif "i've slept well" in query:
                speak("Thats good sir hope you have a fun day")
            elif "i had a good night" in query:
                speak('Thats good sir, hope you have an amazing day')
            elif "thank you you too" in query:
                speak("Im just an assistant so im always good")
            elif "thank you"  in query:
                speak( "no problem sir, i'm glad i could help")
#DE EXIT COMMANDS
            elif "quit" in query:
                speak("Going offline sir, have a good day")
                quit()
            elif "offline" in query:
                speak("Going offline sir, have a good day")
                quit()
            elif "i need to go" in query:
                speak("Have fun sir and i will be here when you come back")
                quit()
            
            
            

