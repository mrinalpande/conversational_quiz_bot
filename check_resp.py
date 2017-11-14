import json
from pprint import pprint
import quiz
import random
from random import randint
import os


greet = ["Greetings to you too!!!\nTo start quiz \"quiz start\"", "Hello, start a quiz type \"quiz start\"", "Hi, go to quiz by typing \"quiz start\""]

#response check method
def check_resp(response):
    
    #writing the string response to a json
    with open('response.json', 'w') as f:
        f.write(response)

    #Using the file to find intent
    with open('response.json') as data_file:    
        data = json.load(data_file)
   
    #Classifying the intents
    if(data['intent']['name']=='greet'):
        print(format(random.choice(greet)))
    
    elif(data['intent']['name']=='quiz_search'):
        quiz.quiz()
        print("To start another quiz type 'quiz start'\nElse keep talking, I am listening")
    
    elif(data['intent']['name']=='affirm'):
        print("I don't get you")
    
    elif(data['intent']['name']=='goodbye'):
        print("Bye Bye")
        exit()
    # print(response)