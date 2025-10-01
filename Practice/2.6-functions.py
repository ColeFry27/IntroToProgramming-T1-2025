def greet():
    print("Hello World!")

# Parameters and arguements

# Create a function that adds two numbers together
def add(x, y):
    print(x+y)
# Can add as many parameters as needed (no limit)
add(10,30)

# Create a function called add_five_numbers that takes five parameters
# one for each number
# print the sum of the  five numbers
# run the functions three times with different arguements
# DON'T OVER THINK FUNCTIONS

# Create function and create parameters
def add_five_numbers(a, b, c, d, e):
    print( a + b + c + d + e )
# Above what the function is intended to do is listed
# Use function and define the paramters 
add_five_numbers(10, 49, 2, 66, 19)
add_five_numbers(1, 2, 3, 4, 5)
add_five_numbers(91, 210, 6, 89, 10)


# Create a function called full_name that prints the concatentation of
# a person's first and last name 
# take input using the input function, then run the function once

def full_name(first, last):
   print(first + last)
# When using inputs for user response put outside of the function like so
# Also use differing nanmes between variables and parameters
first_name = input("enter your first name\n> ")
last_name = input("enter your last name\n> ")
full_name(first_name, last_name)

# Create a function called area_calculator that calculates the area
# of a rectangle. Take length and width as paramters
# Run function thrice no inpuy

def area_calculator(length, width):
    print(length * width)
area_calculator(3, 4)
area_calculator(19, 84)
area_calculator(69, 420)

# Create a function called word_smash that takes two parameters 
# Thw function should simply concatenate the two parameters
# If non-string are given as arguments convert the arguements within the functon to gaurd against non string values
def word_smash(word, other_word):
    print( str(word) + str(other_word))
word_smash("Cat ", " Dog")
word_smash (3, " lizard")

# Createa function called echo that prints a string a number of times
# the function should take two paramters 
# one for the string one for the amount of echoes
# Example- you,5 = yooyouyouyouyou

def echo(word, echo):
    print(str(word) * echo)
echo("dog", 3)

# Create a function called happy_birthday that takes one parameter name
# When the function runs it should print the happy birthday song for thir name

def happy_birthday(name):
    print("Happy Birthday to you, Happy Birthday to you, Happy birthday dear " + str(name) + ", Happy Birthday to you!")
happy_birthday("Will")
