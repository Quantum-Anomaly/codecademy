#---2/11- Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
unique = []
def unique_english_letters(word):
  return len(set(word))
 #return (len(unique))

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("Easel"))

#---3/11- Count x
# Write your count_char_x function here:

def count_char_x(word,x):
  return word.count(x)
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print

#---4/11 - Count Multi
# Write your count_multi_char_x function here:
def count_multi_char_x(word,x):
  return (word.count(x))

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

#---5/11 - Substring Between
# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
  #if none of these are found print the word
  if start not in word or end not in word:
    return word
  #start char's are in the word then return the letters in between the start and end
  else:
    #the +1 here states the letter after the start, and excludes the letter at end to give us the results needed
    return word[word.find(start)+1:word.find(end)]
# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#---6/11 - X length
# Write your x_length_words function here:
def x_length_words(s,x):
  split_s = s.split(' ')
  for word in split_s:
    if len(word) >= x:
      return True
    else:
      return False

# Uncomment these function calls to test your tip function:
#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True

#---7/11 - Check Name
# Write your check_for_name function here:
def check_for_name(sentence,name):
  lower_sentence = sentence.lower()
  if name.lower() not in lower_sentence:
    return False
  else:
    return True
# Uncomment these function calls to test your  function:
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#---8/11 - Every Other Letter
# Write your every_other_letter function here:

def every_other_letter(word):
  return (word[::2])

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print

#---9/11 - Reverse

# Write your reverse_string function here:
def reverse_string(word):
  return word[::-1]
# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print

#---10/11 - Make Spoonerism
# Write your make_spoonerism function here:
def make_spoonerism(word1,word2):
  new_word1=word2[0]+word1[1:]
  new_word2=word1[0]+word2[1:]
  return (new_word1 + " " +new_word2)
# Uncomment these function calls to test your function:
#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a

#---11/11 - Add Exclamation
# Write your add_exclamation function here:
def add_exclamation(word):
  for x in range(len(word)):
    while len(word) < 20:
      word += "!"
    else:
      return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
