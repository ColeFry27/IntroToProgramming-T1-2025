first_word = input("Enter a word.\n> ")
word_another = input("Enter another word.\n> ")
final_word = input("Enter final  word.\n> ")
print(first_word + " " + word_another + " " + final_word)

def  add_three(x, y, z):
    print(int(x) + int(y) + int(z))
x = input("Enter integer.\n> ")
y = input("Enter another integer to be added.\n> ")
z = input("Enter final integer to be added.\n> ")
add_three(x, y, z)

def data_three():
    word = input("Input word.\n> ")
    integer = input("Input integer.\n> ")
    decimal = input("Input decimal number.\n> ")
    int_dec = (integer + decimal)
    print(str(word) + ", " + str(int_dec))
data_three()