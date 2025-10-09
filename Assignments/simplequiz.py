# Simple Quiz
question_one = input("T or F, the sum of 3 + 4 is greater than 8?\n> ")
answer_one = "F"

question_two = input("Intro to programming is taught by?\n> ")
answer_two = "Mr. Osowski"

question_three = input("Y or N, Is Elden ring mid?\n> ")
answer_three = "Yes"

question_four = input("Y or N, Do you code in intro to programming?\n> ")
answer_four = "Yes"

question_five = input("Y or N, Is Bartuc light?\n> ")
answer_five = 'Absolutely'

question_six = input("What is the two number sequence between five and eight?\n> ")
answer_six = "67"

# Store answer as variable ie. if correct a = 1 else wrong a = 0

def tally_score():
    if question_one == answer_one:
        print("1. Correct\n")
        a = 1
    else:
        print("1.Wrong\n")
        a = 0

    if question_two == answer_two:
        print("2. Correct\n")
        b = 1
    else: 
        print("2. Wrong\n")
        b = 0

    if question_three == answer_three:
            print("3. Correct\n")
            c = 1
    else:
            print("3. Wrong\n")
            c = 0

    if question_four == answer_four:
        print("4. Correct\n")
        d = 1
    else: 
        print("4. Wrong\n")
        d = 0
    
    if question_five == answer_five:
        print("5. Correct\n")
        e = 1
    else: 
        print("5. Wrong\n")
        e = 0
    
    if question_six == answer_six:
        print("6. Correct\n")
        f = 1
    else: 
        print("6. Wrong\n")
        f = 0
    print("Score = ")
    print(a + b + c + d + e + f)

tally_score()