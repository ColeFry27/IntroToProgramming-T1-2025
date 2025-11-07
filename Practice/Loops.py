# For Loops
'''
Syntax of a For Loop
    for x  in sequence y
    x: Variable
    y: Sequence (Collection of items to iterate over)

Looping over a list

fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    
Looping over a string
    for letter in "hello":
        print(letter)


Looping over a range

The range() function generates a sequence of numbers,
which is often used in for loops when you want to repeat an action a certain number of times.

    for i in range(5):
        print(i)

- `range(5)` generates numbers from 0 up to, but not including, 5.

- `range(start, stop, step)` is also valid, where `start` is the starting point, 
`stop` is the endpoint, and `step` is the increment.


Common For Loop Patterns
    Accumulating Values
    For loops are commonly used to calculate a sum or product of a sequence of numbers.
    
    numbers = [2, 4, 6, 8]
    total = 0
        for num in numbers:
            total += num
        print(total)

        
Filtering Items
    You can use a for loop to filter specific items from a list based on a condition.

    numbers = [1, 2, 3, 4, 5]
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)

    
Nested For Loops

    A nested for loop is a for loop inside another for loop. 
    This is often used to work with two-dimensional data, like lists of lists.
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()


Using break and continue in For Loops
    break: Stops the loop entirely when a certain condition is met.
    continue: Skips the current iteration and continues with the next one.
    # Using break
    for i in range(5):
        if i == 3:
            break
        print(i)

# Using continue
for i in range(5):
    if i == 3:
        continue
    print(i)

    
games = ["Diablo IV", "Castle Crashers", "The Callisto Protocol", "Terraria"]
# for game in games:
#    print(game)

# Print every number from 1-5 using a for loop
# First number is inclusive! Second is exclusive!
for i in range(0,4):
    print(games[i])

# Printing list and ranking
for i in range (0,4):
    print("Rank " + str(i) + ": " + str(games[i]))

# Print every odd number from 1-100
# i is deleted from memory when the for loop finishes

# Even 
for i in range (0,100,2):
    print(i)

# Odd
for i in range (1,100,2):
    print(i)

for i in range(0,101,10): # Third number (n) tells to go ahead n numbers
    print(i)

# Create a list of 100 random numbers that range from -100 to 100
# Print only positive numbers

import random
# Generating 100 random numbers
random_numbers = []
for i in range (0,100):
    random_numbers.append(random.randint(-100,101))

# 2. Print only positive
for num in random_numbers:
    if num > 0:
        print(num)

# 2. Removing negatives
# Gives error since you attempt to find an index that doesn't exist
for i in range(0, len(random_numbers)):
    if random_numbers[i] < 0:
        random_numbers.pop(i)

print(random_numbers)
'''

# Practice For Loops

for i in range(10,0,-1):
  print(i)

import random
random_numbers = []
for i in range (0,10):
  random_numbers.append(random.randint(0, 101))
  print("Random numbers: " + str(random_numbers))
sum = 0
for num in random_numbers:
  sum = sum + num   
print("Sum: " + str(sum))

five_integers = [2,3,4,5,6]
squares = []
for num in five_integers:
  squares.append(num ** 2)

print(squares)

string = input("Enter a word\n> ").lower()
vowels = "aeiou"
vowel_count = 0
for char in string:
  if char in vowels:
    vowel_count = vowel_count + 1        # x = y + x shorthand: x += 1
print("Vowel Count: " + str(vowel_count))

multiple = int(input("Enter an integer\n> "))
for i in range(0, 10):
  print(str(multiple) + "x" + str(i) + "=" + str(multiple * i))

names = ["William Lahr", "Bart", "Bern", "John"]
for name in names:
  print("\nHello " + str(name) + "!")


# Osowski way
user_num = input("Enter an integer\n> ")

try:
  usernum =  int(user_num)
except:
    print("Not an Integer")

for i in range(1,10):
    print(str(user_num) + "x" + str(i)+ "=" + str(usernum*i))
  