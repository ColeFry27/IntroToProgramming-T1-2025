# Craeting a function
# Observe concatenation below on price and rate ( converted to string from float)
def calculate_tax( item, price, rate ):
    print("The amount of tax to be collected on a " + str(price) + " dollar " + item + " is " + str((.01*price*rate)))
    
calculate_tax("Lego set", 120.39, 0.6875)