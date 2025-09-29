# First question, asks what your favorite animal is
animal = input("What is your favorite animal?\n> ")
# Answers first question while adding on a bit of personality to the response
print("Your favorite animal is " + animal + " how interesting!")

# Asks if there is any specific trait for the animal to help identify it
traits = input("What is a trait of " + animal + "'s?\n> ")
# Responds with touch of personality
print(traits + "How interesting!")

# Asks what type of consumer the animal is
consumes = input("Is your animal a herbivore, omnivore, or carnivore?\n> ")
#Responds to the question with what kind of consumer it is
print("It is an " + consumes + ".")

# Questions the user where the animal lives 
where =  input("Where does the " + animal + " live?\n> ")
# Answers question with user response with the addition of Wow!
print("Your animal lives in " + where + ". Wow!")

# Asks what color the animal is
color = input("What color(s) is the " +animal + "?\n>")
# responds using user answer
print(color + "!")

# Riddles the user if the program had asked why they liked the animal
why = input("Did I ever ask why you like "  + animal + "?\n> ")
# Inserts user answer
print(why)

# Adds onto the last question 
response = input("Oh, so why is it your favorite?\n> ")
# Says the reasoing for why the user likes the animal
print("Because " + response)

# Asks if the animal has any special features
special_feature = input("Does " + animal + " have any special features? Such as flight or venom?\n> ")
# States special feature
print(special_feature)

# Asks if user has ever seen
ever_seen = input("have you ever seen any " + animal + "s in your life?\n> ")
# Asks why
print("How come?") 

# asks where the animal lives
land_water = input("Does the " + animal + " live on land or underwater?\n>")
# print user answer
print(land_water)                  

# Recap user answers
animal_again = input("Your favorite animal is?")
print(animal_again + ", it has the trait of " + traits + ", it is a " + consumes + ", lives " + where + ".") 
print("The " + animal + " is the color " + color + ", you like the " + animal + " because  " + response + ".")
print("The " + animal + " has the special feature " + special_feature + ", and it lives on " + land_water + ".")
