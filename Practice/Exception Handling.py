# Exception handling
#  is a crucial aspect of programming that allows developers to manage errors + exceptional conditions
# primarily done using try  and except blocks

'''
# Basic syntax of exception handling
try:
    # Code that may raise an exception
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Cannot divide by zero.")

# If the division by zero occurs, the code inside the EXCEPT block will bexeecuted andthe program won't crash
# To catch everything wrute except without a condition


# Catching Multiple exceptions
try:
    # Code that may raise different exceptions
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

    
# Using the Finally Clause
# Used to run code regardless of whether an exception occured or not
file = None
try:
    file = open("example.txt", "r")
    # Perform file operations
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file:
        file.close()
'''

# Practice
'''
def times_two():
    num = input("Enter a number\n> ")
    try:
     print(int(num) * 2)
    except:
        print("You must enter an integer")
        times_two()
times_two()
'''

# Randomization
# MUST IMPORT the random module 
import random 

# Generating random numbers
'''
r = random.randint(0,10)
print(r)
'''

x = random.uniform(0, 10)
print(x)