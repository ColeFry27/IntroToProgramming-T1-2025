'''
answer = input("Write a short sentence.\n> ")

# How to do multiple string functions 

print(answer.upper().strip().replace("bad", "good"))
'''

#   Better way to do it 
x = input("Write a sentence.\n> ")
print(x.upper())
print(x.strip())
print(x.replace("bad", "good"))

if x.endswith("."):
    print(True)
else:
    print(False)