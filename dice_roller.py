#Dice roll program.
#Describe the purpose of this program here.

import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def roll():
    print("rolling.....")
    roll = random.randint(1,6)


def show_dice():
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)


roll
time.sleep(1)
show_dice(roll)
#print starts with a lower case p.
#between the first if and final else should be elif.
#on the first print in the show_dice function, it prints (S1) but it's actually called (s1).
#in the roll function rand.randing(7) should be random.randint(1,6)
#The last 3 lines are indented when they shouldn't be.
#in the show_dice function the = should be == for all if and elif functions.
