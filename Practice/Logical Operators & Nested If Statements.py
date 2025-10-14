#   Nested If Statements
#   Example
age = 20
has_permission = True

if age >= 18:
    if has_permission:
        print("Access granted")
    else:
        print("Access denied: Permission required")
else:
    print("Access denied: Age restriction")

# First checks if age is greater than 18
# If true, it checksif has_permission is true
# Not using this can cause a lack of nuance inbetween the two seperate access denied states