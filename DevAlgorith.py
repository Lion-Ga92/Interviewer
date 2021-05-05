import random
import sys

a = "hello"
b = "bye"
c = "ciao"
allow_1 = [a, b, c]
def Algorith_recu(d, something):
    global allow_1

    if d > 1:
        a = "hello"
        b = "bye"
        c = "ciao"

        pick_let = random.randrange(0,4)

        if pick_let == 0:
            print("hello my friend")
            input("press")
            print("You have removed", a)
            Algorith_recu(d-1, allow_1.remove(a))
        

        elif pick_let == 1:
            print("Good bye my friend")
            input("press")
            print("You have", b)
            Algorith_recu(d-1, allow_1.remove(b))

        elif pick_let == 2:
            print("Ciao caro meo")
            input("press")
            print("You have removed ", c)
            Algorith_recu(d-1, allow_1.remove(c))

    else:
        print("Exit now ")
        exit()


Algorith_recu(4, allow_1)