# Branches are decided based off the choices needed to get there e.g. choice order 14325, Branch 1.4.3.2.5


# Note to self exit_or_leave_tower is undefined? Issue present!


# Ending Functions
def adventure_exploit_ending():
   print("Pityful.")
   print("Game over")


def bribe_gunned():
   print("Reference simulation mastermind vs dingus")
   print("Mastermind > Dingus")


# Starting Function (Branch 0)
def adventure_start():
   print("Inside of a great tower, you stand face to face with a crystal ball. Do you:")
   print("1. Gaze upon the ball")
   print("2. Stand around")
   
   crystal_ball_choice = input("> ")
   if crystal_ball_choice == "1":
       gaze_crystal()
   elif crystal_ball_choice == "2":
      stand_around()
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

# Branch 2.1
def the_game():
   print("START HERE!")
   print(" __  ______________________________________________________________________ ")
   print("|    |__   ____  ________| |_ _|___ |     |     ______ | __ | __ __________|")
   print("| |______| ____  |  _______|   |   ______ | __| |____ ______| |____________|")
   print("|__ | ___|________________________ | _______|_______|________  |________   |")
   print("| ______| |_____| ________ |____ __|  _______ |__________ ||_____ _________|")
   print("|__ __|_____  |__ ___ ____|__ |__ _| |  _________| ____| _________|____ ___|")
   print("|  ____|___________|_________ _|___| |__ __| ___ | | ___ ___| __| ___|___ _|")
   print("|___________ _________ ___________ | | __|__ |___ ___|__ __|__________ ____|")
   print("|   |________|________________ |___| |_ _| ____ ___| ____| ___| ______  ___|")
   print("|_________________ ___________ ____| |_____ |___ ____|__  _______|_________|")
   print("| ___| __ _||___|__ ____|____ _____| |__ |__ |___|___  ___|________ ||____ |")
   print("| |_____| ________________  _______| |  ____|____ _____|________________ __|")
   print("|_______________________| __|______| | _|_ _____|___ |___ ___| _____|__ ___|")
   print("|  _____||_______ _____|___ _______| |____ _____|___ __| _________| ___|_ _|")
   print("|__ ________________| ______|__ ___| |_ ___|__ __|___ ___|___ ___|__ ______|")
   print("| ____|___ ____|___ ___| ____|___ _| | __|__ __|_______ ||___ |___ __|____ |")
   print("|___ |_____________________________| |________ |____ |_______||________ |_ |")
   print("|________| _____||___| ______ |____| | ______________|____ ______|___ |_ __|")
   print("|_____|_____________________ _____ | |____________________________________ |")
   print("| _____ ||____ |____ ____|__ ______| |___ __| _____|_______|| _____|___ ___|")
   print("|__ _______________| |____|   ____ | |__|__ ___|____________|__ ___________|")
   print("|___ ____||____ __|_____|__________| |__|__ __|_ |_|_______|____________  _|")
   print("||_ ___|____ | ___|____ | _____ ___|_|__________________________________| _|")
   print("|________| | __________________ |       |__ |_  _| ____||______| __ | _____|")
   print("|____ __ __| __| __|____________|   X   |___|___|__________  _____________ |")
   print("|_____|__ ____|___|___ ________ |__   __|__________ ||______________ ||____|")
   print("|__|___ |||________________ |___|______ |_____________ |_____|_______ |__ _|")
   print("|__ ____| ________________|__ ___|_________|_______ ||_______|_ __|____ |_ |")
   print("|__ |_____________ _______|__ __|___ _______________|___ ||_________ ___| _|")
   print("| __|__ ________|____ ||___ ___|___ _|__ __ |___ ||_______ ||______| |____ |")
   print("|__ ____| _______||___ ____|_  ||____  ___|___|_ | _____|___ |_ __|_______ |")
   print("|__ |____________||_ ___|______| ___|__ ____|__ ___|___| ____|________ ||__|")
   print("|__________________________________________________________________________|")
   game_answer = input("> ")
   if game_answer == "The Moon Haunts You":
      print("Time for you to start the actual game!")
      adventure_start()
   else:
      print("Not right, try again!")
      the_game()


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


   upper_class_choice = input("> ")
   if upper_class_choice == "1":
       bribe()
   elif upper_class_choice == "2":
       exploit_poor()
   elif upper_class_choice == "3":
       evil_dude()
   elif upper_class_choice == "4":
       help_others()


# Branch 1.1.1.1
def bribe():
   print("Which politician do you chose to bribe:")
   print("1. Zeeple Zorp, POTUS")
   print("2. Gleeple Glorp, VP")
   print("3. Bogos Binted, House Speaker")
   print("4. King Bob")


   bribe_choice = input("> ")
   if bribe_choice == "1":
       zeeple_zorp()
   elif bribe_choice == "2":
       gleeple_glorp()
   elif bribe_choice == "3":
       bogos_binted()
   elif bribe_choice == "4":
       king_bob()
# Branch 1.1.1.1.1
def zeeple_zorp():
   print("You attempt to bribe President Zeeple Zorp. You fail miserably and end up in federal prison. How do you plan to escape?")
   print("1. Use soup to corrode the bars")
   print("2. Steal the keys from the guard...you hunger grows")


# Branch 1.1.1.1.1.1 (Ending)
def soup_corrode():
   print("You use your weekly soup meal from the kitchen to slowly corrode the bars.")
   print("You end up passing away from old age before any thing happens to the bars... the bars were stainless steel")
   print("Game Over")


# Branch 1.1.1.1.1.2 (Ending)
def steal_keys():
   print("The prison guard walks by and accidently drops his keys, however, a slice of bread also lies right outside your door.")
   print("You fashion a makeshift lasso from bedsheets and reach for the key...")
   print("But Bread Tastes Better Than Key")
   print("You end up with the slice of bread and satiated hunger")
   print("Game Over")




# Branch 1.1.1.1.2 (Ending)
def gleeple_glorp():
   print("Your attemps to bribe the Vice President, Gleeble Glorp, but end up getting gunned down by secret service")
   bribe_gunned()


# Branch 1.1.1.1.3
def bogos_binted():
   print("Just wondering, did you get your photos printed?")
   print("1. Bogos Binted?")
   print("2. What Photos")
   bogos_binted_choice = input("> ")
   if bogos_binted_choice == "1":
       what_bogos_binted()
   elif bogos_binted_choice == "2":
       what_photos()


# Branch 1.1.1.1.3.1
def what_bogos_binted():
   print("Zeeple zorp, foople floop, gleebo gloople glop moordle flooz.")
   print("1. Photos Printed?")
   print("2. Bogos Binted!")
   what_bogos_choice = input("> ")
   if what_bogos_choice == "1":
       photos_printed()
   elif what_bogos_choice == "2":
       bogos_binted_exclamation()


# Branch 1.1.1.1.3.1.1
def photos_printed():
   print("Did you get your photos printed?")
   print("1. Yes")
   print("2. No")
   photos_printed_choice = input("> ")
   if photos_printed_choice == "1":
       yes()
   elif photos_printed_choice == "2":
       no()


# Branch 1.1.1.1.3.1.1.1 (Ending)
def yes():
   print("Congratulations, You printed your photos!")
   print("Victory!")


# Branch 1.1.1.1.3.1.1.2 (Ending)
def no():
   print("How dare you.")
   print("Game Over")


# Branch 1.1.1.1.3.1.2 (Ending)
def bogos_binted_exclamation():
   print("Weeple Worp (Victory)!")


# Branch 1.1.1.1.3.2 (Ending)
def what_photos():
   print("Bruh,")
   print("Game Over, next time zeeple zorp bogos binted.")


# Branch 1.1.1.1.4
def king_bob():
   print("Our rightous ruler, King Bob, has been seen taking bananas as a bribe. Do you:")
   print("1. Come clean")
   print("2. Steal the Crown")
   print("3. Assassinate King Bob")
   king_bob_choice = input("> ")
   if king_bob_choice == "1":
       come_clean()
   elif king_bob_choice == "2":
       steal_crown()
   elif king_bob_choice == "3":
       assassinate_king()


# Branch 1.1.1.1.4.1 (Ending)
def come_clean():
   print("King Bob is forced to resign and you are cherished for exposing the wrongdoings.")
   print("Victory!")


# Branch 1.1.1.1.4.2 (Ending)
def steal_crown():
   print("Stealing the Crown takes meticolous work. Look at the maze and find your way to the crown.")
   print("Hint: Use < for left, > for right, ^ for up, and ! for down.")
   print("The Crown is the + in the center!")
   print ("Start with < or >, then go towards you path.")


   print("      Start Here!       ")
   print(" ________    _________ ")
   print("| _________|______  __|")
   print("|__ | __|____________ |")
   print("| _______|   |___  | _|")
   print("|_ ____| | + | ______||")
   print("| __ |__ |   |__ _____|")
   print("|_ |__| _____|______  |")
   print("|_______|_____________|")
   maze_answer = input("Enter input here: ")
   if maze_answer == "<<!>!<!>!<!>!>^>^":
       print("You've got the crown!")
       print("Victory!")
   else:
       print("You've gotten caught!")
       print("Game Over!")


# Branch 1.1.1.1.4.3 (Ending)
def assassinate_king():
   print("Violence is never the answer you fool.")
   print("Game Over, you'll be forever scarred for your actions.")




# Branch 1.1.1.2 (Ending)
def exploit_poor():
   print("I pity the fool who choses to exploit the poor.")
   adventure_exploit_ending()


# Branch 1.1.1.3
def evil_dude():
   print("What kind of evil dude do you want to be?")
   print("You don't...\n You don't always have to be...\n the bad guy")
   print("1. Super Villian")
   print("2. Prime Evil")
   print("3. Redemption driven")
   print("4. Uncle Poop")


   choice_evil_dude = input("> ")
   if choice_evil_dude =="1":
       super_villian()
   elif choice_evil_dude == "2":
       prime_evil()
   elif choice_evil_dude == "3":
       redemption_driven()
   elif choice_evil_dude == "4":
       uncle_poop()


# Branch 1.1.1.3.1
def super_villian():
   print("Villany shall prevail, you powers are:")
   print("1. Spit acid")
   print("2. Increase the amount of electrons in each atom by 1")
   print("3. Vaporize matter")


   super_villain_power = input("> ")
   if super_villain_power == "1":
       spit_acid()
   elif super_villain_power == "2":
       increase_electrons()
   elif super_villain_power == "3":
       vaporize_matter()
# Branch 1.1.1.3.1.1
def spit_acid():
   print("You chose to spit acid? Disgusting\n Who is your nemesis?")
   print("1. Megamind")
   print("2. Moon Knight")
   print("3. I've conquered the world")


   spit_acid_nemesis = input("> ")
   if spit_acid_nemesis == "1":
       mega_mind()
   elif spit_acid_nemesis == "2":
       moon_knight()
   elif spit_acid_nemesis == "3":
       conquered_world()
# Branch 1.1.1.3.1.1.1
def mega_mind():
   print("Megamind is YOUR arch nemisis. What is your final battle?")
   print("1. Fight Megamind in his acid proof lair")
   print("2. Suprise Megamind when hes getting groceries")
   print("3. Meet Megamind face to face in a all or nothing battle in a 'plain' field")


# Branch 1.1.1.3.1.1.1.1 (Ending)
def acid_proof_lair():
   print("You chose to find Megamind in his lair that nullifies your powers")
   print("Megamind destroys you and strips away your powers, leaving you as a civilian in his empire")
   print("Should've though smarter\n Game Over")


# Branch 1.1.1.3.1.1.1.2 (Ending)
def suprise_megamind():
   print("Suprising Megamind was a choice well made. Megamind succumbs to your acid and you triumph over your nemesis.")
   print("Victory! You've won over the challenges of your nemesis Megamind")


# Branch 1.1.1.3.1.1.1.3 (Ending)
def all_nothing_battle():
   print("You and Megamidn stand within twenty feet of each other.\n He makes the first move by throwing his robots towards you.\n You use your acid spit to vaporize all of the robots")
   print("However while you were destracted you lost track of Megamind...")
   print("The last thing you here before it all dissapears is Will Ferell laughing behind you...")
   print("Game Over, dude")




# Branch 1.1.1.3.1.1.2 (ENDING)
def moon_knight():
   print("No one can champion over Moon Knight, The Fist of Khonshu. You have chosen poorly")
   print("Moon Knight no diffs, SKill issue on your part")
   print("Game over")


# Branch 1.1.1.3.1.1.3
def conquered_world():
   print("You've conquered the world quickly...")
   print("Due to your quick conquering many people have grown to resent you. Do you:")
   print("1. Resign as supreme leader")
   print("2. Extinguish the flames of rebellion")
   conquer_choice = input("> ")
   if conquer_choice == "1":
       resign()
   elif conquer_choice == "2":
       extinguish_rebellion()


# Branch 1.1.1.3.1.1.3.1 (Ending)
def resign():
   print("You resign from your position as supreme leader and the worlds balance is restored. Maybe you were always the good guy")
   print("Victory!")


def extinguish_rebellion():
   print("What do you use to extinguish the rebellion?")
   print("1. Force")
   print("2. Comprimise")
   print("3. Resign")
   extinguish_choice = input("> ")
   if extinguish_choice == "1":
       extinguish_force()
   elif extinguish_choice == "2":
       extinguish_comprimise()
   elif extinguish_choice == "3":
       extinguish_resign()


# Branch 1.1.1.3.1.1.3.1.1 (Ending)
def extinguish_force():
   print("The use of force was, well, foolish.\n The rebellion only gained traction and over throws you swiftly.")
   print("Game Over, next time don't be the bad guy, ;)")
  
# Branch 1.1.1.3.1.1.3.1.2
def extinguish_comprimise():
   print("Comprimise lacked efficieny in the mid 19th century. Luckily, its not the 1850's, and the rebellion agreed to comprimise. Do you:")
   print("1. Back stab and eradicate the rebellion")
   print("2. Resign and allow the world to return to peaceful interactions")
   comprimise_choice = input("> ")
   if comprimise_choice  == '1':
       back_stab()
   elif comprimise_choice == "2":
       resign()


# Branch 1.1.1.3.1.1.3.1.3.1 (Ending)
def back_stab():
   print("Backstabbing the foolish rebellion was an excellent choice, supreme leader.\n You have chosen well")
   print("Congratulations, you have championed over all the feeble minded people who have chosen foolishly.\n YOU WIN!")


# Branch 1.1.1.3.1.1.3.1.3.2 (Ending)
# REUSES resign()


# Branch 1.1.1.3.1.1.3.1.3 (Ending)
def extinguish_resign():
   resign()




# Branch 1.1.1.3.1.2
def increase_electrons():
   print("You want to be able to... Increase the amount of electrons in atoms? Which atoms do you chose:")
   print("No atoms")
   print("ALL ATOMS")
   increase_electrons_choice = input("> ")
   if increase_electrons_choice == "1":
       no_atoms()
   elif increase_electrons_choice == "2":
       all_atoms()
# Branch 1.1.1.3.1.2.1 (Ending)
def no_atoms():
   print("Lame, try again next time")
   print("Game Over")


# Branch 1.1.1.3.1.2.2 (Ending)
def all_atoms():
   print("The universe as we kow it instantly vaporizes into another big bang")
   print("Learn your chemistry next time")
   print("Game Over")


# Branch 1.1.1.3.1.3
def vaporize_matter():
   print("Vaporize matter as you please")
   print("1. Solids")
   print("2. Liquids")
   print("3. Gases")
   vaporize_choice = input("> ")
   if vaporize_choice == "1" or "2" or "3":
       solid_liquid_gas()


# Branch 1.1.1.3.1.3.(123)
def solid_liquid_gas():
   print("The world falls apart, how foolish of your to pick to destroy what you sought to conquer")


# Branch 1.1.1.3.2
def prime_evil():
   print("Which prime evil are you?")
   print("1. Diablo")
   print("2. Mephisto")
   print("3. Ba'al")
   print("4. I want to be a lesser evil")
   prime_evil_choice = input("> ")
   if prime_evil_choice == "1":
       diablo()
   elif prime_evil_choice == "2":
       mephisto()
   elif prime_evil_choice == "3":
       ba_al()
   elif prime_evil_choice == "4":
       lesser_evil()


# Branch 1.1.1.3.2.3
def diablo():
   print("The Lord of Terror. What is your first target:")
   print("1. Nahantu")
   print("2. Hawezar")
   print("3. Storm the high gates")
   print("4. Acquire a vessel")
   diablos_choice = input("> ")
   if diablos_choice == "1":
       nahantu()
   elif diablos_choice == "2":
       hawezar()
   elif diablos_choice == "3":
       storm_gates()
   elif diablos_choice == "4":
       acquire_vessel()


# Branch 1.1.1.3.2.3.1
def nahantu():
   print("Nahantu, spared by Mephisto's wrath, has become rotted with corruption")
   print("1. Make quick work of extinguishing the spiritborn and the spirit realm")
   print("2. Attempt to embody one of the four spirits")
   print("3. Storm the capital")
   nahantu_choice = input("> ")
   if nahantu_choice == "1":
       eradicate_spiritborn()
   elif nahantu_choice == "2":
       embody_spirits()
   elif nahantu_choice == "3":
       storm_capital()


# Branch 1.1.1.3.2.3.1.1 (Ending)
def eradicate_spiritborn():
   print("The Spirits of Nahantu were already left to rot from Mephisto's corruption, Nahantu falls to The Lord of Terror.")
   print("The Lord of Terror's reign has but begun")
   print("Victory!")


# Branch 1.1.1.3.2.3.1.1 (Ending)
def embody_spirits():
   print("Embodying the spirits was a dumb choice from the Lord of Terror. The Spiritborn of Nahantu -")
   print("- realized quickly that the Lord of Terror would be trapped and weakened in the spirit realm")
   print("The Lord of Terror falls in Nahantu, leaving only Mephisto as the only prime evil not regaining strength")
   print("Game Over")


# Branch 1.1.1.3.2.3.1.1
def storm_capital():
   print("Diablo, The Lord of Terror, storms the capital of Nahantu and makes quick work of the council.")
   print("However, Nahantu's undercity used Diablo's reign of terror to overtake Nahantu from Diablo.")
   print("1. Form an alliance with the Dreggs")
   print("2. Attempt to take Nahantu back in the name of Terror")


# Branch 1.1.1.3.2.3.1.1.1 (Ending)
def ally_dregg():
   print("An alliance with the Dreggs of Nahantu's undercity was a great decision")
   print("The Lord of Terror now has an army of Dreggs at his disposal and Nahantu as a base of operations.")
   print("Victory!")


# Branch 1.1.1.3.2.3.1.1.2 (Ending)
def take_nahantu():
   print("The Dreggs of the undercity, although weak in power, are strong in number")
   print("Diablo fell quickly to the army of Dreggs")
   print("Game over")


# Branch 1.1.1.3.2.3.2
def hawezar():
   print("Hawezar, the swamp land, home to the Tree of Whipsers, Hexes, and Curses. The land holds strong connections to the Fell Council...")
   print("1. Search for the Infernal hordes to unite the Fell Council")
   print("2. Ask the Tree of Whispers for a favor")
   hawezar_choice = input("> ")
   if hawezar_choice == "1":
       infernal_compass()
   elif hawezar_choice == "2":
       ask_tree()


# Branch 1.1.1.3.2.3.2.1
def infernal_compass():
   print("In an attempt to find the Fell Council, Diablo acquires an Infernal Compass")
   print("1. Use Infernal Compass")
   print("2. Neglect Compass")
   infernal_compass_choice = input("> ")
   if infernal_compass_choice == "1":
       use_infernal_compass()
   if infernal_compass_choice == "2":
       neglect_infernal()


# Branch 1.1.1.3.2.3.2.2 (Ending)
def ask_tree():
   print("The Tree of Whispers shows no signs of cowering in the presence of the Lord of Terror. Upon asking a question you have sealed your fate")
   print("The Lord of Terror will soon be hung from the Tree of Whispers like the previous fools.")
   print("Game Over, next time don't sign away your life")


# Branch 1.1.1.3.2.3.2.1.1
def use_infernal_compass():
   print("The Infernal Compass points to the Gates of Hell.")
   print("1. Enter")
   print("2. Return to Sanctuary")
   use_infernal_choice = input("> ")
   if use_infernal_choice == "1":
       enter_hell()
   elif use_infernal_choice == "2":
       return_sanctuary()


# Branch 1.1.1.3.2.3.1.2 (Ending)
def neglect_infernal():
   print("Neglecting the Infernal Compass leaves Diablo legion-less. The Wandered soon finds Diablo alone wanderering the areas of Hawezar.")
   print("Diablo fights with the wanderer but falls to their horadric powers.")
   print("Game Over, You will spend enternity in your Soul Stone")




# Branch 1.1.1.3.2.3.2.1.1.1
def enter_hell():
   print("The Infernal Hordes greet you as you enter. Aether Lords and Fiends bow to the presence of The Lord of Terror.")
   print("1. Eradicate the Infernal Hordes")
   print("2. Enter the Fell Council's Chambers")
   enter_hell_choice = input("> ")
   if enter_hell_choice == "1":
       eradicate_infernal_hordes()
   elif enter_hell_choice == "2":
       enter_fell_chambers()
# Branch 1.1.1.3.2.3.2.1.1.2 (Ending)
def return_sanctuary():
   print("Returning to Hawezar without the Fell Council was a choice not even Duriel would make.")
   print("The Rogues of Hawezar gain word of your presence and quickly trap you in a soul stone.")
   print("Game Over, your nothing without your legions")


# Branch 1.1.1.3.2.3.2.1.1.1.1 (Ending)
def eradicate_infernal_hordes():
   print("The Fell Council takes notice to the extermination of their legion, Bartuc, leader of the fell council, and unleashes their full wrath on diablo")
   print("Game Over, the Fell Council judges thee unworthy")


# Branch 1.1.1.3.2.3.2.1.1.1.2 (Ending)
def enter_fell_chambers():
   print("The Fell Council is displeased by your presence. Ismail the Accursed and Geleb the Flame eradicate and sense of terror you caused.")
   print("And as your essence dissapears back into the depths of Hell, The Fell Council mocks you...")
   print("Game Over")


# Branch 1.1.1.3.2.3.3
def storm_gates():
   print("Empowered as the soul embodiment of evil, you ascend to fight the arch angels and end the eternal conflict.")
   print("There you see Tyreal, Archangel of Justice")
   print("1. Fight Tyreal")
   print("2. Ignore Tyreal and unleash your legions of Hell across the High Gates.")
   storm_gates_choice = input("> ")
   if storm_gates_choice == "1":
       fight_tyreal()
   elif storm_gates_choice == "2":
       unleash_hell()


# Branch 1.1.1.3.2.3.3.1 (Ending)
def fight_tyreal():
   print("Tyreal makes quick work of you. Have fun in your Soul Stone")
   print("Game Over")


# Branch 1.1.1.3.2.3.3.2 (Ending)
def unleash_hell():
   print("Your Legions storm through the high gates and destroy everything")
   print("The Eternal conflict dwindles as your efforts have left only Tyreal barely alive")
   print("Victory")




# Branch 1.1.1.3.2.3.4
def acquire_vessel():
   print("You require a vessel, of whom to you corrupt?")
   print("1. Neyrelle")
   print("2. Lorath")
   vessel_choice = input("> ")
   if vessel_choice == "1":
       neyrelle()
   elif vessel_choice == "2":
       lorath()


# Branch 1.1.1.3.2.3.4.1 (Ending)
def neyrelle():
   print("Neyrelle's close connections with the wanderer lead do your demise.")
   print("Game Over, maybe choose a better vessel like Mephisto did with Akarat")


# Branch 1.1.1.3.2.3.4.2 (Ending)
def lorath():
   print("Lorath the last true Horadrim easily traps you in a soul stone.")
   print("Game Over, fool")


# Branch 1.1.1.3.2.2
def mephisto():
   print("The Lord of Hatred. What is your first choice?")
   print("1. Manipulate the wanderer to entrap you in a soulstone")
   print("2. Send Astaroth, Duke of Hellfire, to storm the Druid stronghold")
   print("3. Manipulate Ba'al and Diablo into being trapped in the Black Soulstone")
   mephisto_choice = input("> ")
   if mephisto_choice == "1":
       manipulate_wanderer()
   elif mephisto_choice == "2":
       send_astaroth()
   elif mephisto_choice == "3":
       manipulate_prime_evils()


# Branch 1.1.1.3.2.2.1 (Ending)
def manipulate_wanderer():
   print("By manipulating the wanderer you end up in a soul stone. Then you drive the wanderer to find Akarat's tomb...")
   print("Inside of Akarat's tomb you leave the soul stone and enter Akarat's corpse and use it as a vessel of hatred...")
   print("Victory!")


# Branch 1.1.1.3.2.2.2 (Ending)
def send_astaroth():
   print("Astaroth plunges the stronghold into enternal hellfire. The Druids manifest as spirits suffering eternally")
   print("Victory?")


# Branch 1.1.1.3.2.2.3 (Ending)
def manipulate_prime_evils():
   print("Mainpulating Ba'al and Diablo leads to only all of you ending up in the black soul stone")
   print("Game Over")






# Branch 1.1.1.3.2.3
def ba_al():
   print("The Lord of Destruction. What clan do you turn to ash first:")
   print("1. The Barbarian Sanctuary")
   print("2. The Horadric Vault")
   ba_al_choice = input("> ")
   if ba_al_choice == "1":
       barbarian()
   elif ba_al_choice == "2":
       horadric_vault()


# Branch 1.1.1.3.2.3.1 (Ending)
def barbarian():
   print("The very sanctuary built upon your destruction falls to it again.")
   print("Victory!")


# Branch 1.1.1.3.2.3.2 (Ending)
def horadric_vault():
   print("The Horadric Vault is heavily fortified with many horadrim standing gaurd")
   print("You are forced to cower away in respect to the fact that you are needed for more sinister destruction")
   print("Game Over")


# 1.1.1.3.2.4
def lesser_evil():
   print("Which Lesser Evil:")
   print("1. Belial, Lord of Lies")
   print("2. Duriel, Lord of Pain")
   print("3. Andariel, Maiden of Anguish")
   print("4. Azmodan, Lord of Sin")
   lesser_evil_choice = input("> ")
   if lesser_evil_choice == "1":
       belial()
   elif lesser_evil_choice == "2":
       duriel()
   elif lesser_evil_choice == "3":
       andariel()
   elif lesser_evil_choice == "4":
       azmodan()
# 1.1.1.3.2.4.1 (Ending)
def belial():
   print("The Lord of Lies, apprentice to Mephisto, trapped away inside of the Realm of Lies")
   print("Game Over, my guy you literally chose to be a lame villian of a prime evil?")


# 1.1.1.3.2.4.2 (Ending)
def duriel():
   print("Lord of Pain, and King of Maggots. You pest")
   print("Game over")


# Branch 1.1.1.3.2.4.3 (Ending)
def andariel():
   print("Maiden of Anguish, an insufferable bossfight. Better luck next time")
   print("Game Over")


# Branch 1.1.1.3.2.4.4 (Ending)
def azmodan():
   print("The Lord of Sin, come on dude choose better.")
   print("Game Over")


#  Branch 1.1.1.3.3 (Ending)
def redemption_driven():
   print("Vengeance is not the way")
   print("Game over")


# Branch 1.1.1.3.4
def uncle_poop():
   print("The legendary man who makes the world go round")
   print("1. Play Diablo IV")
   print("2. Play Elden Ring")
   unc_poop_choice = input("> ")
   if unc_poop_choice == "1":
    diablo_iv()
   elif unc_poop_choice == "2":
    elden_ring()


# Branch 1.1.1.3.4.1
def diablo_iv():
   print("What Build?")
   print("1. Evade Spiritborn")
   print("2. Legion Necromancer")
   print("3. Shadow Step Rogue")
   diablo_iv_choice = input("> ")
   if diablo_iv_choice == "1":
       evade_spiritborn()
   elif diablo_iv_choice == "2":
       legion_necromancer()
   elif diablo_iv_choice == "3":
       shadow_step_rogue()


# Branch 1.1.1.3.4.1
def evade_spiritborn():
   print("A pristine choice")
   print("1. Fight Lilith")
   print("2. Fight Uber Lilith")
   choice_fight_lilith = input("> ")
   if choice_fight_lilith == "1":
       fight_lilith()
   elif choice_fight_lilith == "2":
       fight_uber_lilith()


# Branch 1.1.1.3.4.1.1 (Ending)
def fight_lilith():
   print("The Final Boss of the Campaign")
   print("You can take the boss down with ease and collect you achievement. Sancutaury's protector")
   print("You WIN!")


# Branch 1.1.1.3.4.1.2 (Ending)
def fight_uber_lilith():
   print("Uber Lilith the Final boss of the game itself, capable of one shotting any build at any stage of progression.")
   print("You have chosen your own death")
   print("Game Over, You were smote instantly.")


# Branch 1.1.1.3.4.2
def legion_necromancer():
   print("What Minion")
   print("1. Mages")
   print("2. Golems")
   necromancer_choice = input("> ")
   if necromancer_choice == "1":
       mages()
   elif necromancer_choice == "2":
       golems()


# Branch 1.1.1.3.4.2.2
def mages():
   print("Skeletol Mages, deal great damage while having the capabilities of immortality")
   print("1. Fight Mephisto")
   print("2. Fight Ashava, The Pestilent")
   mages_choice = input("> ")
   if mages_choice == "1":
       fight_mephisto()
   elif mages_choice == "2":
       fight_ashava()


# Branch 1.1.1.1.3.4.2.2.1 (Ending)
def fight_mephisto():
   print("The Lord of Hatred and Deception, Mephisto easily manipulates you into feeling immence hatred.")
   print("Once you've been manipulated you were nothing more than a coughing baby fighting a thermo-nuclear bomb.")
   print("Game Over. Remeber mind, body, and spirit work in unison.")


# Branch 1.1.1.1.3.4.2.2.2 (Ending)
def fight_ashava():
   print("Ashava, the dragon permanently afflicted with poison.")
   print("The battle is long but un the end Ashava falls to your mages")
   print('Victory!')


# Branch 1.1.1.3.4.2.2
def golems():
   print("Golems, high health, high damage, big bang for your buck, a great choice to aid in a build no reliant on minions")
   print("1. Fight Wandering Death, Death given Life")
   print("2. Fight Bartuc, Lord of Chaos")
   golems_fight = input("> ")
   if golems_fight == "1":
       fight_death()
   elif golems_fight == "2":
       fight_bartuc()
# Branch 1.1.1.3.4.2.2.1 (Ending)
def fight_death():
   print('Wandering Death, the soul embodiment of what everything must meet.')
   print("Wandering Death easily uses its soulrift beam to steal yor soul and leave nothing but a lifeless carcass")
   print("You will now suffer enternitu seeing only from Death's soul orb. Game Over")


# Branch 1.1.1.3.4.1.2.2 (Ending)
def fight_bartuc():
   print("Bartuc Lord of Chaos has but one true nemesis, the Vizqatuur.")
   print("Finding Bartuc in the chambers of the Fell Council you must dodge his attacks,")
   print("Hint: Your the #, and the attacks are - and %. And the lane your character stands in is the bottom lane! (2 Lanes)")
   print("Example dodge patter: >><>><")
   print("Use < for up and > down")
   print(" _________________ ")
   print("|     -    %     -|")
   print("| # -   -     %   |")
   print("|_________________|")
 
   dodge_attacks = input("Enter Dodge Pattern:")
   if dodge_attacks == "<><><>":
       print("You've slain Bartuc and banished his chaos legions out from Sanctuary. Congratulaions,\n Victory!")
   else:
       print("Bartuc's reign of chaos continues with one less obstacle...\n Game Over")




# Branch 1.1.1.3.4.3
def shadow_step_rogue():
   print("A masterfull class full of traps and tricks")
   print("1. Fight Azmodan")
   print("2. Fight Astaroth")
   rogue_fight_choice = input("> ")
   if rogue_fight_choice == "1":
       fight_azmodan()
   elif rogue_fight_choice == "2":
       fight_astaroth()


# Branch 1.1.1.3.4.1.3.1 (Ending)
def fight_azmodan():
   print("Azmodan, the least evil of the lesser evils, succumbs easily to your attacks. Attacks Azmodan once hes weak!")
   print("Hint: use arrows to indicate direction, ^ for up, > for right, and < for left. Take the easiest path to the Weak spot (X)")
   print("You are the #, you want to hit the X, and an < or > goes fully left or fully right, an ^ goes up once.")
   print("Example attack: The X is to the left three space up: ^^^< would be your answer")
   print(" _________________ ")
   print("|            v    |")
   print("|          <**}   |")
   print("|         ~( X )  |")
   print("| #>      (_____) |")
   print("|           ^  ^  |")
   print("|_________________|")
   attack_pattern = input("Attack:")
   if attack_pattern == "^>":
       print("Azmodan has fallen, he returns to the depths of Hell and Sanctuary has been saved from the Lord of Sin. Congratulations Wanderer,\n you have felled a lesser evil,\n You Win!")
   else:
       print("The Lord of Sin ceases his moment to escape. Azmodan still wanders Sanctuary...\n Game Over")


# Branch 1.1.1.3.4.3.1 (Ending)
def fight_astaroth():
   print("The Duke of Hellfire, warlord of Hell, and guardian of Mephisto's realm. Comes prepared with his Amalgam of Rage.")
   print("You never stood a chance wanderer.")
   print("With one blow Astaroth turns you into food for the Amalgam of Rage. Game Over")


# Branch 1.1.1.3.4.2 (Ending)
def elden_ring():
   print("I lowkey don't know how to play Elden Ring, so play Diablo IV next time!")
   print("Try Again, Game Over")


# Branch 1.1.1.4
def help_others():
   print("How generous, how do you begin?")
   print("1. End Hunger")
   print("2. End poverty")
   help_choice = input("> ")
   if help_choice == "1":
       end_hunger()
   elif help_choice == "2":
       end_poverty()


# Branch 1.1.1.4.1
def end_hunger():
   print("Ending Hunger is a hefty task, but feasible. How do you begin?")
   print("1. Bacon, Bacon, Bacon")
   print("2. Bagels")
   print("3. Delay solving world issues")
   hunger_choice = input("> ")
   if hunger_choice == "1":
       bacon_thrice()
   elif hunger_choice == "2":
       bagels()
   elif hunger_choice == "3":
       delay_solving()


# Branch 1.1.1.4.1.1 (Ending)
def bacon_thrice():
   print("Bacon, a mastercraft of creation. The Greatest way to solve hunger!")
   print("Bacon is dispensed worldwide in the greatest effort to end hunger, and\n\n\n\n\n\n\n It\n\n WORKS!")
   print("Victory, you ended world hunger!")

# Branch 1.1.1.4.1.2 (Ending)
def bagels():
   print("Bagels? Who likes those? NEXT!")
   print("Game Over, bagels are a fools gold.")

# Branch 1.1.1.4.1.3 (Ending)
def delay_solving():
   print("Ah... A classic, procastinate, put it off, don't do it!")
   print("Now we wait!")
   print("Game Over! Why wait? Do it now!")

# Branch 1.1.1.4.2 (Ending)
def end_poverty():
   print("Ending Poverty? Have Fun achieving nothing!")
   print("Game Over, You lost cause your to ambitious!")

# Branch 1.1.2
def middle_class():
   print("You chose to live with security. You next move is:")
   print("1. Work your 9-5")
   print("2. Quit your job and trade stocks")
   print("3. Start a double life")
   print("4. Reflect on your life")
   middle_class_choice = input("> ")
   if middle_class_choice == "1":
       nine_five()
   elif middle_class_choice == "2":
       trade_stocks()
   elif middle_class_choice == "3":
       double_life()
   elif middle_class_choice == "4":
       reflect_life()


# Branch 1.1.2.1 (Ending)
def nine_five():
   print("Working 9 to 5? \n Makes you lose your mind doesn't it?")
   print("How about I let you start again?")
   print("Game end, choose smarter next time!")


# Branch 1.1.2.2
def trade_stocks():
   print("Buy what stocK?")
   print("1. Dr. Pepper")
   print("2. Nintendo")
   print("3. Tesla")
   stock_choice = input("> ")
   if stock_choice == "1":
       dr_pepper()
   elif stock_choice == "2":
       nintendo()
   elif stock_choice == "3":
       tesla()
  
# Branch 1.1.2.2.1 (Ending)
def dr_pepper():
   print("The Worlds best creation, if god had a favorite drink, it be Dr. Pepper. Your money was well invested your stocks increase ten-fold!")
   print('Congratulations, your rich!')
   print("Your moving up in the world!")
   upper_class()


# Branch 1.1.2.2.2 (Ending)
def nintendo():
   print("Whats that? Mhm, yep, is see. So nintendo games are $90 each now...")
   print("You Lost all your money :=[")
   print("Game Over, your broke! Do not pass Go, go straight to Jail!")
# Branch 1.1.2.2.3 (Ending)
def tesla():
   print("Eletric Vehicles? Vehicle of the future, and I lowkey can't think of how to continue this path so try another!")
   print("Game Over, lack of inginuity!")

# Branch 1.1.2.3 (Ending)
def double_life():
   print("A double life? Choose your double life!")
   adventure_start()


# Branch 1.1.2.4 (Ending)
def reflect_life():
   print("Look back!")
   gaze_crystal()


# Branch 1.1.3
def lower_class():
   print("You chose to live life through constant struggle. Do you:")
   print("1. Perservere")
   print("2. Apply for a job")
   print("3. Live under a rock")
   print("4. Become an evil dude")
   lower_choice = input("> ")
   if lower_choice == '1' or "2" or "3" or "4":
       all_lower()


# Branch 1.1.3.1 (ENDING)
def all_lower():
   print("I don't know what you thought would happen when you chose poorly, pun intended")
   print("Game Over")


# Branch 1.1.4
def noble():
   print("Live honorably and you will never be dissatisfied. Do you:")
   print("1. Become a wizard")
   print("2. Become a Knight")
   print("3. Become royalty")
   print("4. Become full of malicious intent")
   noble_choice = input("> ")
   if noble_choice == "1":
       wizard()
   elif noble_choice == "2":
       noble_life()
   elif noble_choice == "3":
       noble_life()
   elif noble_choice == "4":
       malicious()


# Branch 1.1.4.1 (Ending)
def wizard():
   print("You've become a wizard with a mysterious crystal ball. You choose to test it!")
   adventure_start()


# Branch 1.1.4.2-3 (Ending)
def noble_life():
   print("To live noblely is to live honorably!")
   print("Victory! Your life goes on enternally preserved in history as the Great Noble")


# Branch 1.1.4.4 (Ending)
def malicious():
   print("Just an evil guy I guess,")
   evil_dude()


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
   print("2. Throw the nothing burger away")
   manifest_choice = input("> ")
   if manifest_choice == "1":
       eat_nothing_burger()
   elif manifest_choice == "2":
       throw_nothing_burger()


# Branch 1.2.1.1 (Ending)
def eat_nothing_burger():
   print("You ate nothing and your hunger grows, here try this")
   print("Game over, your hunger puts you in an inverse food coma!")


# Branch 1.2.1.2 ( ENDING)
def throw_nothing_burger():
   print("Nothing Happens")
   print("1. Manifest another nothing burger")
   print("2. Use Crystal Ball")
   throw_burger_away_choice = input("> ")
   if throw_burger_away_choice == "1":
       manifest_again()
   elif throw_burger_away_choice == "2":
       nothing_burger_reuse_ball()


# Branch 1.2.1.2.1 (ENDING)
def manifest_again():
   manifest_notburger()


# Branch 1.2.1.2.2 (ENDING)
def nothing_burger_reuse_ball():
   adventure_start()

# Branch 1.2.2
def hallucinate_notburger():
   print("A nothing burger appears before you. Do you:")
   print("1. Reach out to the nothing burger")
   print("2. Steathily grab the nothing burger")
   hallucinate_choice = input("> ")
   if hallucinate_choice == "1":
       reach_nothing_burger()
   elif hallucinate_choice == "2":
       stealth_nothing_burger()


# Branch 1.2.2.1 (Ending)
def reach_nothing_burger():
   print("You reach out and the Burger dissapears into, nothing!")
   print("USE STEALTH! Game Over!")


# Branch 1.2.2.2 (ENDING)
def stealth_nothing_burger():
   print("You suprise the nothing burger and finally get to eat it!")
   eat_nothing_burger()


# Branch 1.2.3
def disregard_notburger():
   print("Your vision of a nothing fades, then you realize you were never in a tower but instead at a burger joint. Do you:")
   print("1. Order a plain burger")
   print("2. Order a custom burger")
   print("3. Leave the burger joint")
   print("4. Order a nothing burger")
   disregard_choice = input("> ")
   if disregard_choice == "1":
       plain_burger()
   elif disregard_choice == "2":
       custom_burger()
   elif disregard_choice == "3":
       leave_burger_joint()
   elif disregard_choice == "4":
       order_nothing_burger()
# Branch 1.2.3.1 (Ending)
def plain_burger():
   print("A Burger with Cheese. Classic!")
   print("Victory! Enjoy your burger!")


# Branch 1.2.3.2
def custom_burger():
   print("Customize your burger, ALL OR NOTHING!")
   print("1. All")
   print("2. Nothing")
   custom_burger_choice = input("> ")
   if custom_burger_choice == "1":
      all_burger()
   elif custom_burger_choice == "2":
      nothing_nothing_burger()

# Branch 1.2.3.2.1 (Ending)
def all_burger():
   print("A burger with everything? Que Interesante!")
   print(" ___________________ ")
   print("(                   )")
   print(" ------------------- ")
   print(" ################### ")
   print(" ******************* ")
   print(" ################### ")
   print(" ___________________ ")
   print("(                   )")
   print(" ------------------- ")
   print("Your burger has arrived. enjoy! \n VICTORY!")


# Branch 1.2.3.2.2 (Ending)
def nothing_nothing_burger():
   print("You want a burger with nothing... As you wish")
   print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
   print("Game Over")

# Branch 1.2.3.3 (ENDING)
def leave_burger_joint():
   print("Somethings preventing your from leaving...")
   disregard_notburger()


# Branch 1.2.3.4 (ENDING)
def order_nothing_burger():
   nothing_burger()


# Branch 1.2.4 (LOOP)
def conitinue_look_notburger():
   print("You continue to stare at your nothing burger.")
   nothing_burger()


# Branch 1.3
def ps3():
   print("You now have a PS3 in your inventory. Do you:")
   print("1. Take the PS3 out of your inventory")
   print("2. Continue to look into the crystal ball")


   ps3_choice = input("> ")


   if ps3_choice == "1":
       ps3_inventory()
   elif ps3_choice == "2":
       continue_look_crystal_ball()


# Branch 1.3.1
def ps3_inventory():
   print("The PS3 now stands before you. Do you:")
   print("1. Search for an outlet")
   print("2. Disassemble the PS3")
   print("3. Return the PS3")
   print("4. Grab a controller")
   ps3_choice = input("> ")
   if ps3_choice  == "1":
      search_outlet()
   elif ps3_choice == "2":
      dissasemble()
   elif ps3_choice == "3":
      return_ps3()
   elif ps3_choice == "4":
      grab_controller()

# Branch 1.3.1.1
def search_outlet():
   print("After scouring the tower for hours you still can't find an outlet. Do you:")
   print("1. Dissasemble the PS3")
   print("2. Continue search")
   search_choice = input("> ")
   if search_choice == "1":
      dissasemble()
   elif search_choice == "2":
      continue_search()

# Branch 1.3.1.1.2
def continue_search():
   print("Where do you look?")
   looks = input("> ")
   if looks == "Here":
      print("Here?")
      continue_search()
   else:
      print(str(looks) + "?\n Ok,")
      print("Are you sure, cause I don't really know where " + looks + " is.")
      sure = input("> " + "\n (yes or no)")
      if sure == "yes":
         adventure_start()
      elif sure == "no":
         continue_search()

# Branch 1.3.1.2
def dissasemble():
   print("How to you dissasemble a PS3?")
   print("1. Youtube tutorial")
   print("2. Screwdriver")
   print("3. De-atomizer")

# Branch 1.3.1.3
def return_ps3():
   print("The PS3 vanishes into a mist, here we go again\n\n\n")
   gaze_crystal()

# Branch 1.3.1.4
def grab_controller():
   print("The controller slips into your hands. Do you play:")
   print("1. Diablo III")
   print("2. Elden Ring")
   print("3. The Game")


# Branch 1.3.2
def continue_look_crystal_ball():
   print("You continue to stare into the crystal ball. Then something appears")
   gaze_crystal()


# Branch 1.4
def cloudy_mist():
   print("The crystal ball shows a cloudy mist. Do you:")
   print("1. Wait for the mist to disappear")
   print("2. Leave the tower")
   print("3. Look back into the crystal ball")
   print("4. Search inventory")


   cloudy_mist_choice = input("> ")
   if cloudy_mist_choice == "1":
       wait_mist()
   elif cloudy_mist_choice == "2":
       leave_tower()
   elif cloudy_mist_choice == "3":
       look_back_crystal_ball()
   elif cloudy_mist_choice == "4":
       search_inventory()


# Branch Exit or Leave
def exit_or_leave_tower():
   print("How do you choose to leave?")
   print("1. Elavator")
   print("2. Stairs")
   print("3. Portal")

# Branch 1.4.1 
def wait_mist():
   print("The mist begins to slowly dissapear. As it clears up you notice the crystal ball was, infact, a bowling ball. Do you:")
   print("1. Go to the local bowling alley")
   print("2. Add bowling ball to your inventory")
   print("3. Leave the tower")
   print("4. Drop the bowling ball")


# Branch 1.4.2
def leave_tower():
   exit_or_leave_tower()


# Branch 1.4.3
def look_back_crystal_ball():
   gaze_crystal()


# Branch 1.4.4
def search_inventory():
   print("Inside you inventory you find. A rock, Scissors, and Glue. Do you:")
   print("1. Eat the glue")
   print("2. Search for paper")
   print("3. Break the scissors into two seperate blades")
   print("4. Close inventory")


# Branch 2 

def stand_around():
   print("Why?")
   print("Play this game while you wait.")
   confidence()


def confidence():
   print("ARE YOU SURE?")
   print("Confident?")
   print("1. Yes, I can wait")
   print("2. No I want to start the game now!")
   confident_choice = input("> ")
   if confident_choice == "1":
    the_game()
   elif confident_choice == "2":
      gaze_crystal()



adventure_start()