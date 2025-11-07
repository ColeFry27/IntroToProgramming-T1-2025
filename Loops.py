# 1 
for i in range(10,0,-1):
  print(i)

numbers = [3,1,2,3,4,5,6,7,8,9]
sum = 0
for num in numbers:
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
    vowel_count = vowel_count + 1
print("Vowel Count: " + str(vowel_count))

multiple = int(input("Enter a number between 1 and 10\n> "))
for i in range(0, 11):
  print(str(multiple) + "x" + str(i) + "=" + str(multiple * i))

names = ["Alice", "Bob", "Cooper", "Daniel"]
for name in names:
  print("\nHello " + str(name) + "!")
  
  
