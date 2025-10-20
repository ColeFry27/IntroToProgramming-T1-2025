import random
def fortune_teller():
    luck = 0
    print("The mystical fortune teller has arrived, seek forth  your fortune!")
    lucky_number = input("Enter lucky number.\n> ")
    future = input("How far in to the future?\n> ")
    happens = input("Will this happen?\n> ")    
    lucky_number = random.randint(0, 10)
    future = random.uniform(10, 20)
    happens = "Yes" ;not "No"
    if lucky_number >= 0 and lucky_number <= 5:
        luck = luck + 20
    elif lucky_number > 5 and lucky_number <= 9:
        luck = luck + 10
    else:
        luck = luck + 5


    print("Luck = " + str(luck))
fortune_teller()