#Lesson strings
#1/12 - Intro
favorite_word = "Learning"
print(favorite_word)

#---
#2/12 - All lists

my_name = "Chris"
first_initial = my_name[0]

#---
#3/12 - Slicing a string
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5] #first 5 letters  of last name
print (new_account)

temp_password = last_name[2:6] #3rd letter to the 6th letter
print (temp_password)

#---
#4/12 - Concatenating strings
first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name,last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name
#new account has to be below the function above to return the new variable
new_account = account_generator(first_name, last_name)
print(new_account)

#---
#5/12 - More string Slicing
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name,last_name):
  account_name = first_name[2:] + last_name[4:]
  print(account_name)
  return account_name
temp_password = password_generator(first_name,last_name)

#---
#6/12 - Negative indices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
#print the second to last character
second_to_last = company_motto[-2]
print(second_to_last)
#splice the last 4 of the motto to a new variable
final_word = company_motto[-4:]
print(final_word)

#---
#7/12 - Strings are immutable (cant change once created)
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[-2:]

#---
#8/12 - Escape Characters
#if you want to include special characters the escape character is \ to include
password = "theycallme\"crazy\"91"

#---
#9/12 - Iterating through Strings
def get_length(word):
  counter = 0
  for i in word:
    counter += 1
  return counter

#---
#10/12 - Strings and Conditionals

word = "slant"
def letter_check(word,letter):
  for i in word:
    if i == letter:
    	return True
  else:
    return False
#---
#11/12 - Strings and Conditionals Pt 2
def contains(big_string,little_string):
  if little_string in big_string:
    return True
  else:
    return False
def common_letters(string_one, string_two):
  #creates a list to store the common letters
  common = []
  #itirates through string one to check against string two and not already in the list
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
#---
#12/12 - # REVIEW:
first_name = "bob"
last_name = "tanner"
def username_generator(first_name,last_name):
  username = first_name[:3] + last_name[:4]
  return username
#new account has to be below the function above to return the new variable
new_account = username_generator(first_name, last_name)
print(new_account)

def password_generator(new_account):
	password = new_account[-1] + new_account[:-1]
	return password
