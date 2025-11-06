# Indexing starts at index 0
'''
Creating a list:
x (Variable) = [a, b, c, d]
(a, b, c, d, are all parameters)

Creating a simple list
    fruits = ["apple", "banana", "cherry"]


An empty list
    empty_list = []


Accessing List Items
    To access an item from a list, use its index within square brackets
    The first item has an index of 0, the second an index of 1, and so on.
    Negative indexing is also allowed, where -1 refers to the last item, -2 to the second last, etc.

Accessing the first item
    print(fruits[0])  # Output: "apple"


Accessing the last item using negative indexing
    print(fruits[-1])  # Output: "cherry"



# Modifying Lists

ADDING ITEMS
    append()
        Adds an item to the end of the  list
    insert()
        Adds an item at a specified index
    extend()
        Adds (Combines) multiple items (from another list or iterable) to the end of the list


Example:
    Adding items to the list
    fruits.append("orange")      # ["apple", "banana", "cherry", "orange"]
    fruits.insert(1, "grape")    # ["apple", "grape", "banana", "cherry", "orange"]

REMOVING ITEMS
    remove()
        Removes the first occurence of a specified item
    pop()
        Removes an item by its index and returns it. IF no index is specified, it removes the last item
    clear()
        Removes ALL items from the list, making it empty

Example:
    Removing items from the list
    fruits.remove("banana")  # Removes "banana" from the list
    fruits.pop(2)            # Removes the item at index 2 ("cherry" in this case)


Method	                        Description
    append(x)	                Adds an item (x) to the end of the list.
    insert(i, x)	            Inserts an item x at index i.
    remove(x)	                Removes the FIRST occurrence of the item x.
    pop([i])	                Removes and returns the item at index i; removes the last item if i is NOT specified.
    clear()	                    Removes ALL items from the list.
    index(x)	                Returns the index of the FIRST occurrence of item x.
    count(x)	                Returns the count of item x in the list.
    sort()	                    Sorts the list in ASCENDING order.
    reverse()	                Reverses the items in the list. 
    extend(iterable)	        Adds items from another iterable to the end of the list.


EXTRA FUNCTIONS
    len()
        Returns the number of given items in a list
    max(x)
        Returns the highest 
    min(x)
        Returns the lowest 



    

LIST COMPREHENSIONS
    List comprehensions provide a concise way to create lists by generating 
    and processing items in a single line of code. 
    They often replace traditional for loops to create new lists based on some criteria or transformation.

Example:
    Creates a list of square numbers from 0 - 10

squares = [x**2 for x in range(10)]  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''

'''
Practice
                      0(-7)   1(-6)   2(-5)     3(-4)       4(-3)        5(-2)        6(-1)
    allergy_food = ["Apples", "Pears", "Plums", "Cherries", "Peaches", "Nectarines", "Tomatos"]
    print(allergy_food)

    print(allergy_food[-7])

    allergy_food.append("Fresh Pitted Fruits")
    print(allergy_food)

    allergy_food.clear()
    print(str(allergy_food) + "1")

    allergy_food.append("Fruits")
    allergy_food.append("Fresh")
    allergy_food.append("Pitted")
    print(allergy_food)

    allergy_food.pop(1)
    print(allergy_food)

    # When indexing for a specific part of a list, terminal will return an error if index is outside of range!
    # E.g. allergy_food has index 0 and 1 (At the current point where 0 is indexed, at the beginning it ranges from 0-6)

    print(allergy_food[0])
'''

# List Practice 

fruits = ["Mango", "Strawberries", "Kiwi", "Pineapple", "Grapes"]
print(str(fruits[0]) + ", " + str(fruits[4]))

added_fruit = input("Add a fruit!\n> ")
fruits.append(added_fruit)
print(fruits)

fruits.remove(added_fruit)

remove_fruit = input("Remove a fruit!\n> ")
if remove_fruit == "Mango":
    fruits.remove("Mango")
    print(fruits)
elif remove_fruit == "Strawberries":
    fruits.remove("Strawberries")
    print(fruits)
elif remove_fruit == "Kiwi":
    fruits.remove("Kiwi")
    print(fruits)
elif remove_fruit == "Pineapple":
    fruits.remove("Pineapple")
    print(fruits)
elif remove_fruit == "Grapes":
    fruits.remove("Grapes")
    print(fruits)
else:
    print("Fruit not in the original list, try again!")

fruit_duplicate = ["Mango", "Apple", "Banana", "Grape", "Cranberry", "Orange", "Tangerine", "Apple", "Banana", "Grape"]
print(fruit_duplicate.count("Apple"))
