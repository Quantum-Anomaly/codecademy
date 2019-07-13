#Lesson
#---1/9 - Dicitonaries
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6  "garage": 2 "driveway": 1}

print(sensors)

#You’ve just added a sensor to your "pantry", and it reads 22 degrees. Add this pair to the dictionary on line 1
#Remove the # in front of the definition of the dictionary num_cameras
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

#---2/9 - Make a dictionary
#Values can be any type. You can use a string, a number, a list, or even another dictionary as the value associated with a key!
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

#You can also mix and match key and value types. For example:
person = {"name": "Shuri", "age": 18, "siblings": ["T'Chaka", "Ramonda"]}

#---3/9 - Invalid Keys
#We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

#--- 4/9 - Empty dictionary
my_empty_dictionary = {}

#---5/9 - Add a key
my_dict["new_key"] = "new_value"
#start with list
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#add in new key and item
menu["cheesecake"] = 8
#new dictionary list
{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}
#exercise
animals_in_zoo={}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

#---6/9 - Add multiple keys
#Original dictionary
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
#add in more to sensors at once (one line)
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
#Exercise
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

#---7/9 - Overwrite Values
#To overwrite an existing value (add it like it was new with the same key name)
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

#---8/9 - List Comprehensions to dictionaries
#two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#create a dictionary using a list comprehension
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
#zip() combines two lists into a list of pairs
#Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list
#Creates a key : value item in the students dictionary
#Creates a key : value item in the students dictionary
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
#create a variable called zipped_drinks that is a list of pairs between the drinks list and the caffeine list
zipped_drinks = zip(drinks,caffeine)
#print(zipped_drinks)
#Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

#---9/9 - Review
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs,playcounts)}
#print(plays)
#entry should be for the song "Purple Haze" and the playcount is 1
plays["Purple Haze"] = 1
#Update the value for "Respect" to be 94
plays["Respect"] = 94
#dictionary called library that has two key: value pairs
#key "The Best Songs" with a value of plays
#key "Sunday Feelings" with a value of an empty dictionary
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
