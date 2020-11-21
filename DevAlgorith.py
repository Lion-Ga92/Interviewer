import random
import sys


def Algorith_recu(d):
    #id = ["z", "x", "y"]
    #len_of_lid = len(lid)
    #print(len_of_lid)
    #d = lid.pop(-1)

    if d > 0:
        a = "hello"
        b = "bye"
        c = "ciao"

        allow = [a, b, c]
        pick_let = random.randrange(0,4)

        if pick_let == 0:
            print(a)
            input("press")
            allow.remove(a)
            Algorith_recu(d-1)
        

        elif pick_let == 1:
            print(b)
            input("press")
            allow.remove(b)
            Algorith_recu(d-1)

        elif pick_let == 2:
            print(c)
            input("press")
            allow.remove(c)
            Algorith_recu(d-1)

    else:
        print("Exiiiiit")
        exit()


Algorith_recu(3)