def adventure_start():
    print("Inside of a great tower, you stand face to face with a crystal ball. Do you:")
    print("1. Gaze upon the ball")
    print("2. Stand around")
    print("3. Break the crystal ball")
    print("4. Add the crystal ball to your inventory")

    crystal_ball_choice = input(">")
    
    if crystal_ball_choice == "1":
        gaze_crystal()
    elif crystal_ball_choice == "2":
        stand_crystal()
    elif crystal_ball_choice == "3":
        break_crystal_ball()
    elif crystal_ball_choice == "4":
        add_to_inventory()

def gaze_crystal():
    print('A')
    print("You have gazed upon the crystal ball, do you see:")
    print("1. A reflection of yourself")
    print("2. A nothing burger")
    print("3. A PS2")
    print("4. A cloudy mist")

    what_see = input(">")
    print(what_see)

def stand_crystal():
    print("p")
    print("After standing around for several hours, dust begins to collect on the crystal ball. Do you:")
    print("1. Dust the crystal ball")
    print("2. Lick the crystal ball")
    print("3. Look into the crystal ball")
    print("4. Stand around")

def break_crystal_ball():
    print("x")
    print("You broke the crystal ball?\n You've doomed us all. Do you:")
    print("1. Put the shards in your inventory")
    print("2. Eat the glass")
    print("3. Have an existential crisis")
    print("4. A great curse falls upon you. The curse never forgets...")

def add_to_inventory():
    print("W")
    print("You've added the crystal ball to your inventory. Now do you:")
    print("1. Exit the tower")
    print("2. Lay down")
    print("3. Sit down")
    print("4. Ponder")

adventure_start()