fry_faves = {
    "Video Game": "Terraria",
    "Food": "Crazy Dragon Roll",
    "Color": "Green",
    "City": "None",
    "Class": "Intro to Programming"
}


print(fry_faves["Food"])

# Add a new entry
fry_faves["Terraria Class"] = "Ranger - Bows"

# Modify an entry
fry_faves["Color"] = "Purple"

# Remove an entry
fry_faves.pop("City")

# Looping through a dictionary
for key, value in fry_faves.items():
    print(str(key) + ": " + str(value))

print("----------")

print(fry_faves.keys())

print(fry_faves.values())

print(fry_faves.items())

fry_faves.clear()
print(fry_faves)
