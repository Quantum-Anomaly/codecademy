#---
#1/11
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)
#---
#2/11
#for <temporary variable> in <list variable>:
    <action>
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game)
for sport in sport_games:
  print(sport)

#---
#3/11 -  Range in loops
promise = "I will not chew gum in class"
for i in range(5):
  print(promise)

#---
#4/11 - Infinite loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
  #substitue first list to generate infinite loop
  students_period_B.append(student)
  print(student)

  #---
  #5/11 - Break
#You can stop a for loop from inside the loop by using break.
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")
#exercise
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'
for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

#---
#6/11 - Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for n in ages:
  if n < 21:
    #if n is greater than 21 it will print the age otherwise it skips it
    continue
  print(n)

#---
#7/11 - while loops
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []
while len(students_in_poetry) < 6:
  students_in_poetry.append(all_students.pop())
  if len(students_in_poetry) == 5:
    print(list(students_in_poetry))
    break

#---
#8/11 - nested loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
  print(location)
  for i in location:
    scoops_sold += i
print(scoops_sold)

#---
#9/11 - List comprehensions
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)
Python has a convenient shorthand to create lists like this with one line:

usernames = [word for word in words if word[0] == '@']
This is called a list comprehension. It will produce the same output as the for loop did:

["@coolguy35", "@kewldawg54", "@matchamom"]
This list comprehension:

Takes an element in words
Assigns that element to a variable called word
Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
Repeats steps 1-3 for all of the strings in words

#exercise
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

#---
#10/11 - More list comprehensions
messages = [user + " please follow me!" for user in usernames]
This list comprehension:

Takes a string in usernames
Assigns that number to a variable called user
Adds “ please follow me!” to user
Appends that concatenation to the new list called messages
Repeats steps 1-4 for all of the strings in usernames
my_upvotes = [192, 34, 22, 175, 75, 101, 97]
We want to add 100 to each value. We can accomplish this goal in one line:

updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]

#exercise
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [((cval * 9/5)+32) for cval in celsius]
print(fahrenheit)

#---
#11/11 review
#Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits = range(0,10)
#Create a for loop that goes through single_digits and prints out each one.
for a in single_digits:
  print(a)
  #Create a list called squares. Assign it to be an empty list to begin with.
squares = []
#Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.
for b in single_digits:
  squares.append(b**2)
  #After the for loop, print out squares.
print(squares)
#Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
cubes = [digit**3 for digit in single_digits ]
#Print cubes.
print(cubes)
