'''
Return Statement
return is used to send back a result from a finction to its caller. 
This allows the function to produce output that can be used elsewhere in the program.
Example with a return value
def square(number):
    return number * number

    When you call the square(5), the function returns 25. You can store this returned calue ina variable
result = square(5) 
print(result)  # Outputs: 25
'''


# Function with no parameters and no return value
def greet():
    print("Hello, world!")

# Function with one parameter
def greet(name):
    print("Hello, " + name + "!")

# Function with multiple parameters and a return value
def add(a, b):
    return a + b

# Function that calculates and returns an area
def calculate_area(width, height):
    return width * height


'''
Global scope refers to varaibles and functions that are defined OUTSIDE of any function or class,
making them accessible throughout the entire program.

Variables defined in the global scope can be accessed and modified from anywhere in the code, 
including within functions

Global varaibles are typically declared at the top of the script

Example: '''

global_var = 10 # Global variable

def print_global():
	print(global_var) # Accessing global variable

print_global() # Outputs: 10

'''
Local scope refers to variables that are defined within a function or block of code,
This makes them ONLY accesible within that function or block
Example
'''



