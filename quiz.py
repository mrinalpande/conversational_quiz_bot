import json
from pprint import pprint
import random
from random import randint
import os

def quiz():
        # Loading categories
        categories = set()
        for root, dirs, files in os.walk("./OpenTriviaQA_JSON"):
                for name in files:
                        categories.add(name[: -5])
        # print(categories)

        greeting = ['Hi there, how are you doing today!\nI am quizzy, let\'s play a quiz today!', 'Hi I\'m quizzy, your quizmaster!', 'Quizzy here, let\'s start']
        wrong_category = ['Hmm! We currently do not have any quizzes on that.', 'Sorry we don\'t have any questions regarding that.', 'Hmm, pick another one!']
        next_question = ['Here comes the next question!', 'Get ready for the next one!', 'Here comes another']
        correct_answer = ['Correct answer, well done!', 'You\'re smart!', 'You\'re a genius']
        wrong_answer = ['Sorry, wrong answer. Nevermind', 'Wrong! Buck up', 'Nah! Come on!']

        # Engaging user in coversation
        flag = False
        category = ""
        print(random.choice(greeting))
        print('What would you liked to be quizzed on?')
        while flag == False:
                user_response = input()
                if user_response[0] == '@':
                        if user_response[1: ] == 'list_quizzes':
                                for c in categories:
                                        print(c)
                                print()
                                continue
                words = user_response.split(' ')
                common = categories.intersection(set(words))
                if len(common) == 0:
                        print("{} Type @list_quizzes to list categories".format(random.choice(wrong_category)))
                else:
                        common = list(common)
                        category = common[0]
                        print('Alright! One quiz on {} coming right up!'.format(category))
                        print('We score +1 for a correct answer and -0.25 for a wrong one. Enjoy!')
                        print('Type @stop_quiz anytime to quit the quiz')
                        flag = True


        # Open quiz bank for particular category
        dir_path = os.path.join('OpenTriviaQA_JSON')
        with open(os.path.join(dir_path, category + '.json')) as data_file:
                data = json.load(data_file)
        # pprint(data)

        # Start quiz!
        genarated = []
        stop = False
        score = 0

        print('\nHere we go!')
        while stop == False:
                rand = randint(-1, len(data) - 1)
                while rand in genarated:
                        rand = randint(-1, len(data) - 1)
                genarated.append(rand);

                print(data[rand]['question'])
                ct = 'A'
                answer = data[rand]['answer']
                answer_choice = ''
                for c in data[rand]['choices']:
                        print('{}. {}'.format(ct, c))
                        if c == answer:
                                answer_choice = ct
                        ct = chr(ord(ct) + 1)

                user_response = input()
                if user_response[0] == '@':
                        if user_response[1: ] == 'stop_quiz':
                                stop = True
                                print('Thanks for playing. Your final score was {}'.format(score))
                                continue
                response_words = user_response.lower().split(' ')
                answer_words = answer.lower().split(' ')
                answer_choice = answer_choice.lower()

                if answer_choice in response_words or set(answer_words).issubset(set(response_words)):
                        print(random.choice(correct_answer))
                        score += 1
                        print ('Score = {}'.format(score))
                        print(random.choice(next_question))
                else:
                        print(random.choice(wrong_answer))
                        score -= .25
                        print ('Score = {}'.format(score))
                        print(random.choice(next_question))
                print()
