import random
def fortune_teller():
    luck = 0
    print("The mystical fortune teller has arrived, seek forth  your fortune!")
    lucky_number = input("Enter lucky number.\n> ")
    future = input("How far in to the future?\n> ")
    happens = input("Will this happen?\n> ")    
    lucky_number = random.randint(0, 10)
    future = random.uniform(10, 20)
    happens = "Yes" or "No"
    try:
        if lucky_number >= 0 and lucky_number <= 5:
            luck = luck + 20
        elif lucky_number > 5 and lucky_number <= 9:
            luck = luck + 10
        else:
            luck = luck + 5
    except:
        print("Must enter an Integer")
        fortune_teller()
    
    try:
        if future >= 10 and future < 14.999999:
            luck = luck + 5
        elif future >= 15 and future <= 20:
            luck = luck + 1
        else:
            luck = luck + 0
    except:
        print("Must enter Float")
        fortune_teller()

    try:    
        if happens == "Yes":
            luck = luck + 5
        elif happens == "No":
            luck = luck + 1
        else:
            luck = luck + 0
    except:
        print("Must enter a string")
        fortune_teller

    print("Luck = " + str(luck))
fortune_teller()