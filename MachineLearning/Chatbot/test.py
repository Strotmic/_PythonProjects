from email import message
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

from tensorflow.keras.models import load_model

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[0].id)



lemmatizer = WordNetLemmatizer()
intents = json.loads(open('test.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('botV1.h5')

def clean_up_sentence(sentence):
    sentence_word = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_word]
    return sentence_word

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag =[0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_TRESHOLD =0.25
    results =[[i,r] for i, r in enumerate(res) if r> ERROR_TRESHOLD]

    results.sort(key=lambda x: x[1] , reverse=True)

    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability' : str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    result = []
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print('ok')

while True:
    message = input()
    ints = predict_class(message)
    res = get_response(ints, intents)
    
    engine.say(res)
    engine.runAndWait()
