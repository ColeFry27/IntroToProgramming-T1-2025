# Elif Statements
'''
String Functions
Allow you to manipulate and anaalyze text data efficiently
Enable you to perform operations such as transforming, searching, and modifying streings

    str.upper()	    Converts all characters to uppercase	"hello"	"HELLO"

    str.lower()	    Converts all characters to lowercase	"WORLD"	"world"

    str.capitalize()	Capitalizes the first character	"python programming"	"Python programming"

    str.title()	Capitalizes the first character of each word	"python programming"	"Python Programming"

    str.strip()	Removes whitespace from both ends	"   hello   "	"hello"

    str.replace(old, new)	Replaces occurrences of a substring	"hello world"	
    "hello Python" (with str.replace("world", "Python"))

    str.split(separator)	Splits a string into a list based on a separator    
    "one,two,three"	["one", "two", "three"]

    str.join(iterable)	Joins elements of an iterable into a string	["a", "b", "c"]	
    "a-b-c" (with "-".join(["a", "b", "c"]))

    str.find(substring)	Returns the index of the first occurrence of a substring	"hello"	1 (for str.find("e"))

    str.endswith(suffix)	Checks if the string ends with a specified suffix	"filename.txt"	
    True (for str.endswith(".txt"))

# Example of string functions

text = " hello world "

# Uppercase
print(text.upper())  # Output: " HELLO WORLD "

# Lowercase
print(text.lower())  # Output: " hello world "

# Capitalize
print(text.capitalize())  # Output: " hello world "

# Title
print(text.title())  # Output: " Hello World "

# Strip whitespace
print(text.strip())  # Output: "hello world"

# Replace
new_text = text.replace("world", "Python")
print(new_text)  # Output: " hello Python "

# Split
words = "one,two,three".split(",")
print(words)  # Output: ['one', 'two', 'three']

# Join
joined_text = "-".join(["a", "b", "c"])
print(joined_text)  # Output: "a-b-c"

# Find
index = text.find("o")
print(index)  # Output: 4

# Endswith
is_txt_file = "filename.txt".endswith(".txt")
print(is_txt_file)  # Output: True

'''