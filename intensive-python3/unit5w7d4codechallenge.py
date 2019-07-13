#---2/10---Sum Values
#Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary
# Write your sum_values function here:
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
#---3/10 --Even Keys
#Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total_sum = 0
  for value in my_dictionary.keys():
    if value % 2 == 0:
      total_sum += my_dictionary[value]
  return total_sum
# Uncomment these function calls to test your  function:
#it checks to see if key is even{1:5}, if it is it adds the item value to the total_sum
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#---4/10 -- Add ten
#Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary
# Write your add_ten function here:
def add_ten(my_dictionary):
  for value in my_dictionary.keys():
    my_dictionary[value] += 10
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#---5/10 -- values that are Keys
#Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  new_list = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      new_list.append(value)
  return new_list
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#---6/10 -- largest values
#Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
# Write your max_key function here:
def max_key(my_dictionary):
    # .items() here brings both to the table making it easier to get the max value without new variables, and returns the corresponding key
  for key, value in my_dictionary.items():
    if value == max(my_dictionary.values()):
      return key
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

#---7/10 -- Word length dictionary
#Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  #gives the format for how the data is returned. variable word is used as the placeholder and the piece for getting the lenght iterated through each value.
  return {word:len(word) for word in words}
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
#--- 8/10 -- Frequency count
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  return {word:words.count(word) for word in words}
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#---9/10 --
# Write your unique_values function here:
def unique_values(my_dictionary):
  return len(set(my_dictionary.values()))
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#---10/10 -- Count first letter
# Write your count_first_letter function here:
def count_first_letter(names):
  new_dict = {}
  for key, value in names.items():
    if key[0] not in new_dict:
      my_dict.update({key[0] : len(value)})
    else:
      my_dict[key[0]] += len(value)
  return my_dict
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
