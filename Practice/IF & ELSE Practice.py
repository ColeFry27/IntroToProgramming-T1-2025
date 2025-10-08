a = 0
b= 11
c= 58

'''
if True:
    print("If statement ran")
else:
    print("plum")

    
# Statement is evaluated as true so it prints kiwi
if a == 0:
    print("Kiwi")
else:
    print("plum")

    
# Statement is evaluated as false so it prints plum
if a > 0:
    print("Kiwi")
else:
    print("plum")

if a < 0 or b == 10:
    print("kiwi")
else:
    print("plum")

    
if a < 0 and b == 11:
    print("kiwi")
else:
    print("plum")
'''



def check_password():
    real_password = "Fry"
    submitted_password = input("ENTER PASSWORD\n> ")

    if real_password == submitted_password:
        print("Access Granted")
    else:
        print("Access Denied.")
        check_password()

check_password()