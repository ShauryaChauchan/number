from ast import While
import random

randomnum=random.randint(1,9)

chances=0
while chances<3:
    guessnumbers=int(input("Enter a number :"))
    if randomnum==guessnumbers:
        print ("CONGO")
        break
    elif guessnumbers>randomnum:
        print ("you guess is too high")
    else :
        print ("Your guess is too low")
    chances+=1
if not chances <3:
    print ("you lose")