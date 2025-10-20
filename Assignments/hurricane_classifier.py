wind_speed = input("What is the wind speed of the hurricane?\n> ")
if int(wind_speed) < 74:
    print("Tropical Storm")
elif int(wind_speed) >= 74 and int(wind_speed) < 96:
    print("Category 1")
elif int(wind_speed) >= 96 and int(wind_speed) < 111:
    print("Category 2")
elif int(wind_speed) >= 111 and int(wind_speed) < 130:
    print("Category 3")
elif int(wind_speed) >= 130 and int(wind_speed) < 157:
    print("Category 4")
elif int(wind_speed) >= 157:
    print("Category  5")
