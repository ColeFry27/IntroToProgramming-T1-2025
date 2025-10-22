def adventure_start():
    print("Inside of a great tower, you stand face to face with a crystal ball. Do you:")
    print("1. Gaze upon the ball")
    print("2. Stand around")
    print("3. Break the crystal ball")
    print("4. Add the crystal ball to your inventory")

    crystal_ball_choice = input("> ")
    
    if crystal_ball_choice == "1":
        gaze_crystal()
    elif crystal_ball_choice == "2":
        stand_crystal()
    elif crystal_ball_choice == "3":
        break_crystal_ball()
    elif crystal_ball_choice == "4":
        add_to_inventory()

# Branch 1
def gaze_crystal():
    print("You have gazed upon the crystal ball, do you see:")
    print("1. A reflection of yourself")
    print("2. A nothing burger")
    print("3. A PS3")
    print("4. A cloudy mist")

    gaze_choice = input("> ")

    if gaze_choice == "1":
        see_reflection()
    elif gaze_choice == "2":
        nothing_burger()
    elif gaze_choice == "3":
        ps3()
    elif gaze_choice == "4":
        cloudy_mist()

# Branch 1.1
def see_reflection():
    print("Your reflection shows your future. In the future are you:")
    print("1. Upper Class")
    print("2. Middle Class")
    print("3. Lower Class")
    print("4. Noble")

    choice_see_reflection = input("> ")

    if choice_see_reflection == "1":
        upper_class()
    elif choice_see_reflection == "2":
        middle_class()
    elif choice_see_reflection == "3":
        lower_class()
    elif choice_see_reflection == "4":
        noble()

# Branch 1.1.1
def upper_class():
    print("You chose to live lavishly. Do you:")
    print("1. Bribe politicians")
    print("2. Exploit the poor")
    print("3. Become an evil dude")
    print("4. Help others with your wealth")

# Branch 1.1.2
def middle_class():
    print("You chose to live with security. You next move is:")
    print("1. Work your 9-5")
    print("2. Quit your job and trade stocks")
    print("3. Start a double life")
    print("4. Reflect on your life")

# Branch 1.1.3
def lower_class():
    print("You chose to live life through constant struggle. Do you:")
    print("1. Perservere")
    print("2. Apply for a job")
    print("3. Live under a rock")
    print("4. Become an evil dude")

# Branch 1.1.4
def noble():
    print("Live honorably and you will never be dissatisfied. Do you:")
    print("1. Become a wizard")
    print("2. Become a Knight")
    print("3. Become royalty")
    print("4. Become full of malicious intent")

# Branch 1.2
def nothing_burger():
    print("You see a nothing burger? Do you:")
    print("1. Manifest a nothing burger")
    print("2. Hallucinate a nothing burger")
    print("3. Disregard your vision and leave the tower")
    print("4. Continue to look at the nothing burger")

    choice_nothing_burger = input("> ")

    if choice_nothing_burger == "1":
        manifest_notburger()
    elif choice_nothing_burger == "2":
        hallucinate_notburger()
    elif choice_nothing_burger == "3":
        disregard_notburger()
    elif choice_nothing_burger == "4":
        conitinue_look_notburger()

# Branch 1.2.1    
def manifest_notburger():
    print("After manifesting a nothing burger one appears to fill the empty space in the tower. Do you:")
    print("1. Eat nothing burger")
    print("2. Add to inventory")
    print("3. Admire your work")
    print("4. Throw the nothing burger away")

# Branch 1.2.2
def hallucinate_notburger():
    print("A nothing burger appears before you. Do you:")
    print("1. Reach out to the nothing burger")
    print("2. Steathily grab the nothing burger")
    print("3. Ignore your hallucination")
    print("4. Eat nothing burger")

# Branch 1.2.3
def disregard_notburger():
    print("Your vision of a nothing fades, then you realize you were never in a tower but instead at a burger joint. Do you:")
    print("1. Order a plain burger")
    print("2. Order a custom burger")
    print("3. Leave the burger joint")
    print("4. Order a nothing burger")

# Branch 1.2.4
def conitinue_look_notburger():
    print("You continue to stare at your nothing burger.")
    nothing_burger()

# Branch 1.3
def ps3():
    print("You now have a PS3 in your inventory. Do you:")
    print("1. Take the PS3 out of your inventory")
    print("2. Continue to look into the crystal ball")
    print("3. Break the PS3")
    print("4. Leave the tower")

# Branch 1.4
def cloudy_mist():
    print("The crystal ball shows a cloudy mist. Do you:")
    print("1. Wait for the mist to disappear")
    print("2. Leave the tower")
    print("3. Look back into the crystal ball")
    print("4. Search inventory")

# Branch 2
def stand_crystal():
    print("After standing around for several hours, dust begins to collect on the crystal ball. Do you:")
    print("1. Dust the crystal ball")
    print("2. Lick the crystal ball")
    print("3. Look into the crystal ball")
    print("4. Stand around")

    stand_around_crystal_choice =  input("> ")

    if stand_around_crystal_choice == "1":
        dust()
    elif stand_around_crystal_choice == "2":
        lick()
    elif stand_around_crystal_choice == "3":
        relook_into_crystal()
    elif stand_around_crystal_choice == "4":
        stand_around()
    
# Branch 2.1
def dust():
    print("You dust the crystal ball and see that the crystal ball was infact, a bowling ball. Do you:")
    print("1. Go to the local bowling alley")
    print("2. Add bowling ball to your inventory")
    print("3. Leave the tower")
    print("4. Drop the bowling ball")

def lick():
    print("You chose to...\n Lick the crystal ball? You now have:")
    print("1. Mystical Powers")
    print("2. Become the crystal ball")
    print("3. Lose your limbs")
    print("4. Instantly die")

def relook_into_crystal():
    print("You look back into the ball, then you:")
    print("1. Return to start")
    print("2. Zone out")
    print("3. Fall asleep")
    print("4. Leave the crystal ball")

def stand_around():
    print("You chose to stand around. Do you:")
    print("1. Search the tower")
    print("2. Lay down")
    print("3. Look out the window")
    print("4. Look into the crystal ball")

# Branch 3
def break_crystal_ball():
    print("You broke the crystal ball?\n You've doomed us all. Do you:")
    print("1. Put the shards in your inventory")
    print("2. Eat the glass")
    print("3. Have an existential crisis")
    print("4. A great curse falls upon you. The curse never forgets...")

    break_crystal_choice = input("> ")

    if break_crystal_choice == "1":
        put_shards_inventory()
    elif break_crystal_choice == "2":
        eat_glass()
    elif break_crystal_choice == "3":
        existential_crisis()
    elif break_crystal_choice == "4":
        cursed()

# Branch 3.1
def put_shards_inventory():
    print("You've put the shards into your inventory. Do you:")
    print("1. Leave the tower")
    print("2. Attempt to fix the crystal ball")
    print("3. End your journey")
    print("4. Restart your journey")

def eat_glass():
    print("Upon eating the glass you, yourself, have become the crystal ball. Do you:")
    print("1. Go to the local bowling alley")
    print("2. Roll out of the tower")
    print("3. Reform into your former self")
    print("4. Look inwards")

def existential_crisis():
    print("You become very anxious and lose track of what your have done. Do you:")
    print("1. Retrack your steps")
    print("2. Start anew and leave the tower")
    print("3. Review polyatomic ions")
    print("4. Ask a question")

def cursed():
    print("The curse never forgets...")
    print('1. Leave the tower')
    print("2. Teleport away")
    print("3. Attempt to break the curse")
    print("4. Learn wizardery")

# Branch 4 
def add_to_inventory():
    print("You've added the crystal ball to your inventory. Now do you:")
    print("1. Exit the tower")
    print("2. Lay down")
    print("3. Sit down")
    print("4. Ponder")

    choice_inventory = input("> ")

    if choice_inventory == "1":
        exit_or_leave_tower()
    elif choice_inventory == "2":
        lay_down()
    elif choice_inventory == "3":
        sit_down()
    elif choice_inventory == "4":
        ponder()

# Branch 4.1
def exit_or_leave_tower():
    print("You have are leaving the tower, do you leave by:")
    print("1. Stairs")
    print("2. Elevator")
    print("3. Escalator")
    print("4. Call for help")

def lay_down():
    print("You chose to lay down. What do you lay down on:")
    print("1. Couch")
    print("2. Chair")
    print("3. Bed")
    print("4. Floor")

def sit_down():
    print("You sit down in a chair, do you:")
    print("1. Fall asleep")
    print("2. Get up")
    print("3. Grab the remote")
    print("4. Search the chair")

def ponder():
    print("You ponder your situation for years. As time passes monuments of great philosophers, who shadow you, are erected. Do you:")
    print('1. Observe the monuments')
    print("2. Destroy the monuments")
    print("3. Leave the tower")
    print("4. Study quantum theory")

adventure_start()