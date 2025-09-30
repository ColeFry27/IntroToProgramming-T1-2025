'''
Mad Lib Story

Long ago, in (noun),
there was a (noun) that ruled over all (plural noun).
Then came (a name) who was (adjective).
They were the only force capable of beating the (first noun).
However the (first noun) came prepared to deal with (same name),
(First noun) had a (noun) capable of mass destruction.
The (prior noun) was (adjective).
The (prior noun) and (same name) began to (verb -ing) each other for hours
the (verb) was (adverb)
in the end the (prior noun or same name) prevailed!
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

noun_location = input("insert noun\n> ")
ruling_force = input("insert noun\n> ")
place_ruled = input("insert plural noun\n> ")
protaganist = input("insert a name\n> ")
adjective_protaganist = input(insert adjective\n> ")
ruling_force_antaganist = input("insert noun\n> ")
adj_antaganist = input("insert adjevtive\n> ")
main_verb = input("insert verb\n>")
adverb_verb = input("insert adverb\n>")
the_end = input("insert noun or name\n> ")

print("Long ago in " + noun_location + ", there was a " + ruling_force + " that ruled over all " + place_ruled + ". Then came " + protaganist + " who was " + adjective_protaganist + ". They were the only force capable of beating the " + ruling_force + ". However the " + ruling_force + " came prepared to deal with " + protaganist + "," + ruling_force + " had a " + ruling_force_antaganist + " capable of mass destruction. The " + ruling_force_antaganist + " adj_antaganist + ". The " + ruling_force_antaganist + " and " + protaganist + " began to " + main_verb + " each other for hours. The " + main_verb + " was " + adverb_verb + ". In the end the " + the_end + " prevailed!")
