for i in range(1, 21):
    if i == 15:
        break
    print(i)

print("\n")

for i in range(1, 31):
    if i % 2 == 0:
        continue
    print(i)

print("\n")

for i in range(0, 21):
    if i == 20:
        pass        # Break function or print special message
    print(i)

print("\n")

for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

print("\n")

numbers = [1, 2, 3, 4, 5, 6, -1, 7, 8, 9]
sum = 0
for num in numbers:
    sum = num + sum
    if num < 0:
        break
    print(sum)
