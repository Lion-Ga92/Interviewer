import sys

import random

import time



def intro_to_program():

    print("Welcome to the Job interviewer simulator")
    time.sleep(1)
    print("Here you will be given a chance to practice some questions that might pop up in a job interview")
    print("=========BE ADVISED THIS IS JUST A SMALL TEST SCRIPT===========")
    time.sleep(1)
    print("You will be presented with three different scenarios and allowed to prepare mentally for each of them")
    print("After which the system will procceed to the questions.") 
    time.sleep(1)
    print("In order to keep this simple, the questions will not refer to the scenario cutting down the lines of code ")
    print("Our poor, underpaid, overworked developer has to write. 'We did tell you brian to finish your degree!'")
    scenario_picker()

def scenario_picker():
    print("\n")
    time.sleep(1)
    print("Welcome to the scenario picker. A scene will be presented to you and then the questions will follow")
    time.sleep(1)
    print("They will be presented to you in random manner, and you wont be able to see the other scenarios unless ")
    time.sleep(1)
    print("You run the program again")

    scene_pick = random.randrange(1,4)
    time.sleep(1)

    if scene_pick == 1:
        print("\n")
        print(""" You are a high school grad looking for a job at a car wash, you are going to college after 
                  the summer. You are driven and motivated and feel that you would be a very good addition to 
                  the company because you used to volunteer at car wash fundraisers. """)
        input("press enter to continue: ")
        Interview_quests_intro()

    elif scene_pick == 2:
        print("\n")
        print("""You are a college grad, with a post grad education and are looking for a mid level position at
                 a a regional branch of Wells Fargo. You scored great on all your tests, and your thesis on economic
                 models was praised by its committee but due to your focus on your masters you left your previous jobs 
                 in bad terms as it was interrupting your ability to focus on school""")
        input("press enter to continue")
        Interview_quests_intro()

    elif scene_pick == 3:
        print("\n")
        print("""You are a 32 year old male of  a minority population, you are hard working with experience in hard labor 
                jobs. But you lack higher education. You are asking for a job at a car wash due to an injury at work that
                makes it difficult to perform construction or other manual. Labor. Your job record is great, with barely
                any work days missing.""")
        input("press enter to continue") 


        Interview_quests_intro()


def Interview_quests_intro():
    time.sleep(4)
    print("Hello and welcome to our company!")
    time.sleep(1)
    print("It is my understanding that you applied to work for our company, i will ask you a few questions and type a few notes")
    time.sleep(1)
    print("first i would like to ask you to confirm your name? ")
    time.sleep(1)
    print("=======NOTE FROM PROGRAM=======")
    time.sleep(2)
    print("=======RESPOND============")
    time.sleep(4)
    print("====================")
    time.sleep(2)
    print("====================")
    time.sleep(4)
    print("====================")
    time.sleep(1)
    print("====================")
    time.sleep(1)
    print("====================")
    time.sleep(1)
    print("====================")
    print("After this point i will be asking you a few questions, respond to the best of your ability")
    input("press enter to continue ")
    full_questions()



def full_questions(z = 8):

    if z > 0:
        a = "Tell me about yourself"
        b = "Why do you want to work for us?"
        c = "What is your greatest weakness?"
        d = "What assets would you bring to the company?"
        e = "What is your highest level of education?"
        f = "Have you worked at another job previous that is related to this one?"
        g = "Can we contact the references that you provided?"
        h = "Did you leave your last job on good terms?"
        
        #allowed_quests = [a, b, c, d, e, f, g, h]
        allow_lista = [1, 2, 3, 4, 5, 6, 7, 8]
        pick_lett = random.randrange(1, 9)

        if pick_lett == 1 and (pick_lett in allow_lista):
            print("Tell me about yourself")
            #allowed_quests.remove("Tell me about yourself")
            allow_lista.pop(0)
            input("Press entertttttt to get 60 secs. to respond. Press enter once told to move")
            time.sleep(5)
            full_questions(z-1)

        elif pick_lett == 2 and (pick_lett in allow_lista):
            #and (pick_lett in allow_range):
            print("Why do you want to work for us?")
            #llowed_quests.remove("Why do you want to work for us?")
            allow_lista.pop(1)
            input("Press enterr to get 60 secs. to respond. Press enter once told to move")
            time.sleep(5)
            full_questions(z-1)
        
        elif pick_lett == 3 and (pick_lett in allow_lista):
            print("What is your greatest weakness?")
            #allowed_quests.remove("What is your greatest weakness?")
            allow_lista.pop(2)
            input("Press enterraaaa to get 60 secs. to respond. Press enter once told to move")
            time.sleep(5)
            full_questions(z-1)

        elif pick_lett == 4 and (pick_lett in allow_lista):
            print("What assets would you bring to the company?")
            #allowed_quests.remove("What assets would you bring to the company?")
            allow_lista.pop(3)
            input("Press enterrrrrrrrrrrrr to get 60 secs. to respond. Press enter once told to move")
            time.sleep(5)
            full_questions(z-1)

        elif pick_lett == 5 and (pick_lett in allow_lista):
            print("What is your highest level of education?")
            #allowed_quests.remove("What is your highest level of education?")
            allow_lista.pop(4)
            input("Press ente to get 60 secs. to respond. Press enter once told to move")
            time.sleep(5)
            full_questions(z-1)

        elif pick_lett == 6 and (pick_lett in allow_lista):
            print("Have you worked at another job previous that is related to this one?")
            #allowed_quests.remove("Have you worked at another job previous that is related to this one?")
            allow_lista.pop(5)
            input("Press ente to gt 60 secs. to respond. Press enter once told to move")
            time.sleep(5)
            full_questions(z-1)

        elif pick_lett == 7 and (pick_lett in allow_lista):
            print("Can we contact the references that you provided?")
            #allowed_quests.remove("Can we contact the references that you provided?")
            allow_lista.pop(6)
            input("Press ente to get 60secs. to respond. Press enter once told to move")
            time.sleep(5)
            full_questions(z-1)
        
        elif pick_lett == 8 and (pick_lett in allow_lista):
            print("Did you leave your last job on good terms?")
            #allowed_quests.remove("Did you leave your last job on good terms?")
            allow_lista.pop(7)
            input("Press ente to get 60 secs. to respond")
            time.sleep(5)
            full_questions(z-1)
    else:
        print("Thank you for coming to our interview. We will contact you if we have follow up")
        print("questions. Do you have any questions for us?")
        input("Press ente to get 60 secs. to respond. Press enter once told to move")
        time.sleep(5)
        exit()

intro_to_program()