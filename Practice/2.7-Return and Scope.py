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
Local varaibles are created when the function is called and are destroyed when the function exits
They CANNOT be accessed outside of the funtion or block where they're defined
Example
'''
def my_function():
	local_var = 5 # Local variable
	print(local_var) # Accessing the local variable

my_function() # outputs 5
# print(local_var) # Causes an error because the local variable does not exist at the global scope 

'''
Varaible shadowing occurs when a local variable and global varaible has the same name. 
e.g. 
'''
global_var = 20  # Global variable

def my_function():
    global_var = 30  # Local variable shadows the global variable
    print(global_var)  # Outputs: 30

my_function()
print(global_var)  # Outputs: 20 (global variable remains unchanged)

'''
Function Scope
when a function is called, a new local scope is created. Varaibles defined withinthe function a
local to the function and cannot be accessed outside of it.</br></br>

Accessing Global Varaibales in Functions 
To modify a global varraible inside a function, you must use the 'global' keyword to declare that you 
are referring to the global varaible, not creating a local one
e.g.
'''

global_var = 50

def modify_global():
    global global_var
    global_var = 100

modify_global()
print(global_var)  # Outputs: 100