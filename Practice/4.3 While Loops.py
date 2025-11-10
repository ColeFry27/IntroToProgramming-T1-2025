# Condition is a boolean, if false the while loop stops, if true the loop executes
#   SEASON TO TASTE

# while condition:
#   do something
'''
num = 0
continue_adding = True

while continue_adding == True:
    num += 1
    print(num)
    ask = input("Would you like to continue?    Y/N \n> ")
    if ask.lower == "n":
        continue_adding == False



num = 0
continue_add = True

while continue_add = True:
    num += 1
    print(num)

'''

import random


def number_guesser():
    guess = int(input("Guess a number between 0 - 100 \n> "))
    random_num = random.randint(0, 100)
    loop_end = True

    if loop_end == True and guess < random_num:
        while loop_end == True and guess < random_num:
            print("Higher!")
            guess = int(input("Guess a number between 0 - 100 \n> "))
            number_guesser()
    elif loop_end == True and guess > random_num:
        while loop_end == True and guess > random_num:
            print("Lower!")
            guess = int(input("Guess a number between 0 - 100 \n> "))
            number_guesser()
    elif loop_end == True and guess == random_num:
        while loop_end == True and guess == random_num:
            print("Correct")
            loop_end = False

number_guesser()




