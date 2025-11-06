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

'''

games = ["Diablo IV", "Castle Crashers", "The Callisto Protocol", "Terraria"]
for games in games:
    print(games)