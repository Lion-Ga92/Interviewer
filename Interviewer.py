import sys
import random
import time


#THE CODE BELOW IS JUST FLUFF AND PLOT SETTING. 
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

    # I used a simple randrange method to select a number and control flow to have three different scenes for the interviewer
    
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

# THIS FUNCTION IS THE INTRO TO THE INTERVIEW, BUT IT MAINLY SERVES THE PURPOSES OF LEADING TO THE MAIN ALGORYTHM THAT HOUSES THE INTERVIEW 
# QUESTIONS SPECIALLY SINCE THAT FUNCTION WORKS RECURSIVELY. 
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
    time.sleep(1)
    print("====================")
    time.sleep(1)
    print("====================")
    time.sleep(1)
    print("====================")
    print("After this point i will be asking you a few questions, respond to the best of your ability")
    input("press enter to continue ")

    full_questions(9)

a = "Tell me about yourself"
b = "Why do you want to work for us?"
c = "What is your greatest weakness?"
d = "What assets would you bring to the company?"
e = "What is your highest level of education?"
f = "Have you worked at another job previous that is related to this one?"
g = "Can we contact the references that you provided?"
h = "Did you leave your last job on good terms?"

#THE MEAT AND MY HEADACHE INDUCING TROUBLE FOR THE LAST 7 MONTHS. IT IS A FUNCTION THAT WORKS RECURSIVELY. 
# ORIGINALLY IT WAS A RATHER LARGE NUMBER OF LINES OF CODES THAT I DID NOT REALIZE COULD BE DONE WITH JUST A 
# METHOD OF THE RANDOM MODULE.  

quest_list = [a, b, c, d, e, f, g, h]

def full_questions(x):
    if x > 1:
        global quest_list
        choice_1 = random.choice(quest_list)
        print(choice_1)
        quest_list.remove(choice_1)
        input("NOTE: Press enter when you are ready to move")
        print("++++++++++++++++++")
        print("++++++++++++++++++")
        print("                  ")
        print("                  ")
        full_questions(x-1)
    
    else:
        print("Thank you for coming to our interview. We will contact you if we have follow up")
        print("questions. Do you have any questions for us?")
        time.sleep(3)
        exit()


intro_to_program()