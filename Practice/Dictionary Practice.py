names = {
    "Alice": "F",
    "Bob": "Super F",
    "Charlie": "C",
    "Dave": "A",
    "Ethan": "C"
}

student = {
    "name": "Alice", 
    "age": 16, 
    "grade": "A"
    }

print(str(student["name"]) + ", " + str(student["age"]))

student["grade"] = "A+"
print(student)

movies = {
    "Silence of the Lambs": "1991",
    "The Batman": "2022",
    "The Lego Movie": "2014"
}

user_movie = input("Add a movie to the list!\n> ")
release_year = input("What year did it release?\n> ")
movies[user_movie] = release_year
print(movies)

fruits = {
    "Apple": 0.79,
    "Kiwi": 1.79,
    "Tangerine": 2.09,
    "Grapes": 4.19,
    "Strawberry": 6.89
}
remove_fruit = input("Remove a fruit from the list below!\n Apple,\n Kiwi,\n Tangerine,\n Grapes,\n Strawberry\n\n> ")
if remove_fruit.lower == "apple":
    fruits.pop("Apple")
elif remove_fruit.lower == "kiwi":
    fruits.pop("Kiwi")
elif remove_fruit.lower == "tangerine":
    fruits.pop("Tangerine")
elif remove_fruit.lower == "grapes":
    fruits.pop("Grapes")
elif remove_fruit.lower == "strawberry":
    fruits.pop("Strawberry")
print(fruits)