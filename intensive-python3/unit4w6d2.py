#---
#2/13 - Format methods
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title,poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author,poem_author_fixed)

#---
#3/13 -- Splitting strings
line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words)

#---
#4/13 - Spliting strings 2
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
#splits each str between comma as a new list item
author_names = authors.split(",")
print(author_names)
author_last_names = []
#runs through the list and iterates another split
#(using space and taking the last item and appending it to a new list)

for name in author_names:
  last_name = name.split(" ")[-1]
  author_last_names.append(last_name)
#prints  each item in the list
for lname in author_last_names:
  print(lname)

#---
#5/13 - Splitting strings 3
#Newline or \n will allow us to split a multi-line string by line breaks
#and \t will allow us to split a string by tabs
spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""
#They want you to break the poem up into its individual lines.
spring_storm_lines = spring_storm_text.split('\n')

#---
#6/13 - Joining strings
#break strings apart using .split(),
#put them back together using .join()
#'delimiter'.join(list_you_want_to_join)
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
#combine these words into a sentence and save that sentence as the string reapers_line_one
reapers_line_one = ' '.join(reapers_line_one_words)

#---
#7/13 - Joining strings 2
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
#each line of the poem appears on a new line in your string
winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

#---
#8/13 - Strip
#Stripping a string removes
#all whitespace characters from the beginning and end
#list.strip() or list.strip('!') with character
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

#join together all of the lines into a single string that can be used to display the poem
love_maybe_lines_stripped = []
#use .strip() on each line in the list to remove the unnecessary
#whitespace and save it as a new list love_maybe_lines_stripped
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
#.join() the lines in love_maybe_lines_stripped together
#into one large multi-line string, love_maybe_full
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
#Print love_maybe_full
print(love_maybe_full)

#---
#9/13 - Replace
#.replace(). Replace takes two arguments and replaces all instances of
#the first argument in a string with the second argument.
#string_name.replace(character_being_replaced, new_character)
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

#---
#10/13 - find()
#.find() takes a string as an argument and searching the string it was
#run on for that string. It then returns the first index value
#'smooth'.find('t')
#'4'
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)
#Answer: 20

#---
#11/13 - .format()
#.format() takes variables as an argument and includes them in the
#string that it is run on. You include {} marks as placeholders for
#where those variables will be imported
#example:
#def favorite_song_statement(song, artist):
#  return "My favorite song is {} by {}.".format(song, artist)

def poem_title_card(poet,title):
  return "The poem \"{}\" is written by {}.".format(title,poet)

#---
#12/13 - .format() II
#def favorite_song_statement(song, artist):
#    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

#Fix the function by using keywords .format() method.
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc
#Run poem_description with the following arguments
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
#save the results to the variable my_beard_description
my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

#---
#13/13 - # REVIEW:
# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() and f-strings allow you to interpolate a string with variables.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)
#split highlighted_poems at the commas and save it to highlighted_poems_list
highlighted_poems_list = highlighted_poems.split(',')
#print(highlighted_poems_list)

#create a new empty list, highlighted_poems_stripped
highlighted_poems_stripped = []
#iterate through highlighted_poems_list strip away the whitespace and append it to your new list
for line in highlighted_poems_list:
  highlighted_poems_stripped.append(line.strip()) #stripping out whitespace
#print(highlighted_poems_stripped)

#Create a new empty list called highlighted_poems_details
highlighted_poems_details = []

#Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.

for line in highlighted_poems_stripped:
  no_mark = i.split(":")
  highlighted_poems_details.append(no_mark)
	#print(highlighted_poems_stripped)
#separate out all of the titles, the poets, and the publication dates into their own lists
titles = []
poets = []
dates = []
#Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists
for title in highlighted_poems_details:
  titles.append(title[0])
print(titles)
for poet in highlighted_poems_details:
  poets.append(poet[1])
print(poets)
for date in highlighted_poems_details:
  dates.append(date[2])
print(dates)
#write a for loop that uses either f-strings or .format() to prints out the following string for each poem:
#The poem TITLE was published by POET in DATE.
for a in highlighted_poems_details:
    print("The poem " + a[0] + " was published by " + a[1] + " in " + a[2] +".")
