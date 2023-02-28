# importing requests package
import sys
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

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

'''news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)'''

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

NewsFromBBC()