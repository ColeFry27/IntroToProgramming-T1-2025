'''
Mad Lib Story

Long ago, in (noun),
there was a (noun) that ruled over all (plural noun).
Then came (name) who was (adjective).
They were the only force capable of beating the (first noun).
However the (noun) came prepared to deal with (name),
The (noun) had a (noun) capable of mass destruction.
The (noun) was (adjective).
The (noun) and (noun) began to (verb -ing) each other for hours
the (verb) was (adverb)
in the end the (noun) prevailed!
'''

# Pseudocode

"""
Location of story as variable = input enter name of a place
print user response 
ruling force as variable = input name of the ruling force
print user response 
ruled place as variable = input place ruled/thing (make plural if thing)
print user response
Hero name as variable = input name of protaganist
print user response
Describe hero with two adjectives
print user response
Insert plot twist where ruling force is aware of protaginsts plan to collapse the ruling force
Add the item of mass destruction or thing capable of beating the protaganist
Describe the item/thing
The protagnist and antaganist do (verb) 
User describes what they were doing
The  user decides what prevails after the end of the verb
"""

# Mad Lib Code

noun_location = input("Long ago, in [noun]\n> ")
print(noun_location)
ruling_force = input("there was a [noun]\n> ")
print(ruling_force)
place_ruled = input("That ruled over all [plural noun]\n> ")
print(place_ruled)
protaganist = input("Then came (name)\n> ")
print(protaganist)
adjective_protaganist = input(protaganist + " was [adjective]]\n> ")
print(adjective_protaganist)
ruled_place_repeat = input("They were the only force capable of beating the " + ruling_force + ".")
plot_twist = input("however the " + ruling_force + "came prepared to deal with " + protaganist)
antaganist= input("The " + ruling_force + " came prepared to deal with " + protaganist + ".")
ruling_force_antaganist = input("The " + ruling_force + "has a [noun] capable of mass destruction\n> ")
print(ruling_force_antaganist)
adj_antaganist = input("The " + ruling_force_antaganist + " was [adjective\n> ")
print(adj_antaganist)
main_verb = input("The " + protaganist + " and" + ruling_force_antaganist + "began to [verb-ing] each other for hours\n> ")
adverb_verb = input("The " + main_verb + " was [adverb].\n>")
print(adverb_verb)
the_end = input("In the end the [noun main force] prevailed\n> ")
print(the_end)
whole_story = input("enter any key to see finished story.\n> ")
print("Long ago in " + noun_location + " there was a " + ruling_force + " that ruled over all " + place_ruled + "\n" + " then came " + protaganist + " who was " + adjective_protaganist + " They were the only force capable of beating the " + ruling_force + "\n" + " however the " + ruling_force + "came prepared to deal with " + protaganist + " the " + ruling_force + " had a " + ruling_force_antaganist + " capable of mass destruction\n" + "The " + protaganist + " and the " + ruling_force_antaganist + " began to " + main_verb " each other for hours\n")
      