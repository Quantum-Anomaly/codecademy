letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_to_points = dict(zip(letters,points))
letters_to_points[" "] = 0
print (letters_to_points)

def score_word(word):
  point_total = 0
  word = word.upper()
  for x in word:
    if x in letters_to_points:
      point_total += letters_to_points[x]
  return point_total
brownie_points = score_word("brownie")
print(brownie_points)
#Create a dictionary called player_to_words that maps players to a list of the words they have played
player_to_words = {"player1": ["blue","tennis","exit"], "wordNerd":["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "prof reader": ["zap", "coma", "period"]}
#Create an empty dictionary called player_to_points
player_to_points = {}
#Iterate through the items in player_to_words. Call each player player and each list of words words
for player, words in player_to_words.items():
  #Within your loop, create a variable called player_points and set it to 0
  player_points = 0
  #Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input
  for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points
#player_to_points should now contain the mapping of players to how many points they’ve scored
print(player_to_points)
#If you want extended practice, try to implement some of these ideas with the Python you’ve learned
	#play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
  #update_point_totals() — turn your nested loops into a function that you can call any time a word is played
  #make your letter_to_points dictionary able to handle lowercase inputs as well
