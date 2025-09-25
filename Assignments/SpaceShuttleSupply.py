countdown = input("How many seconds left until launch?\n> ")
print(countdown + " seconds left till launch.")

oxygen_tanks = input("How many oxygen tanks are left?\n> ")
print("I have " + oxygen_tanks + " oxygen tanks left.") 

food_packs = input("How many food packs are there for your journey?\n> ")
print("I have "+ food_packs+ " food packs left for my journey.")

water_packs = input("How many water packs are stored on your vessel?\n> ")
print("There remains " + water_packs + " water packs on this ship.")

confirm = input("Confirm amount of supplies.\n> ")
print(confirm + ' all supplies are ready.')

oxygen_tanks_confirm = input("Confirm amount of oxygen tanks.\n> ")
print(oxygen_tanks_confirm + " amount of oxygen tanks confirmed at " + oxygen_tanks)

list_all = input("List all supplies on ship.\n> ")
print(list_all +" there are, "+ oxygen_tanks+ " oxygen tanks, " + food_packs+" food packets, " + water_packs+" water packets, " + oxygen_tanks_confirm +" oxygen tanks, you are now ready for launch.")