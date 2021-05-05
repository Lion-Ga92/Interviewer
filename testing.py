import time
import sys
import random
"""This program is part of a program that is attempting to recreate in the CLI 
    a form of job interview practice environment. Sadly i cant get it to work, as the 
    code is not giving me the correct output. the variables a-h are supposed to be pulled
    out at random. And when the interviewee clicks the input button the question gets removed 
    from the variable quest_list. And another question gets pulled out."""


a = "Tell me about yourself"
b = "Why do you want to work for us?"
c = "What is your greatest weakness?"
d = "What assets would you bring to the company?"
e = "What is your highest level of education?"
f = "Have you worked at another job previous that is related to this one?"
g = "Can we contact the references that you provided?"
h = "Did you leave your last job on good terms?"


quest_list = [a, b, c, d, e, f, g, h]

def full_questions(x):
    if x > 1:
        global quest_list
        choice_1 = random.choice(quest_list)
        print(choice_1)
        quest_list.remove(choice_1)
        input("Press Enter")
        full_questions(x-1) 
        
    else:
        print("Thank you for coming to our interview. We will contact you if we have follow up")
        print("questions. Do you have any questions for us?")
        input("Press ente to get 60 secs. to respond. Press enter once told to move")
        time.sleep(3)
        exit()
        

full_questions(9)