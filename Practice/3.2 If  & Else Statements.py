#   If statements are also known as a conditional statement
#   If statment written as so

#  if condition: 
    # Code to execute if the condition is true
#   e.g.
number = 5
if number > 0:
    print("The number is positive>")

# Else statements 
# The else keyword is used to execute a block of  code if the condition in the if statement is false
#   e.g.
number = -3

if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")

'''
   else statement is reliant on a corresponding if statement above it
   else statements do not take a condition 
   if you have an IF statement then you DO NOT need an ELSE statement
   if you have an ELSE statement then you NEED an IF statement
   CANNOT print both the IF and ELSE statements at the same time due to the ELSE's condition being if the IF fails
'''