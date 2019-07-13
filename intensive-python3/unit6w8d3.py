#---1/9 -- Inheritance
# If the bulk of a class’s definition is useful, but we have a new use case that is distinct from how the original class was used, we can inherit from the original class
# class User:
#   is_admin = False
#   def __init__(self, username)
#     self.username = username
#
# class Admin(User):
#   is_admin = True
#   User as our base class. We want to create a new class that inherits from it, so we created the subclass Admin. In the above example, Admin has the same constructor as User. Only the class variable is_admin is set differently between the two.
class Bin:
  pass
class RecyclingBin(Bin):
  pass

#---2/9 -- Exceptions
#   An Exception is a class that inherits from Python’s Exception class
#   issubclass(ZeroDivisionError, Exception)
# # Returns True
# Above, we checked whether ZeroDivisionError, the exception raised when attempting division by zero, is a subclass of Exception. It is, so issubclass returns True.
# class KitchenException(Exception):
#   """
#   Exception that gets thrown when a kitchen appliance isn't working
#   """
#
# class MicrowaveException(KitchenException):
#   """
#   Exception for when the microwave stops working
#   """
#
# class RefrigeratorException(KitchenException):
#   """
#   Exception for when the refrigerator stops working
#   """
# def get_food_from_fridge():
#   if refrigerator.cooling == False:
#     raise RefrigeratorException
#   else:
#     return food
#
# def heat_food(food):
#   if microwave.working == False:
#     raise MicrowaveException
#   else:
#     microwave.cook(food)
#     return food
#
# try:
#   food = get_food_from_fridge()
#   food = heat_food(food)
# except KitchenException:
#   food = order_takeout()
# Define your exception up here:
class OutOfStockException(Exception):
  """"
  You are currently out of stock!
  """
# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock

  def buy(self, color):
    if self.stock[color] <= 0:
      raise OutOfStockException("The {color} candles are out of stock".format(color=color))
    else:
      self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')

#---3/9 -- Overriding Methods
# An overridden method is one that has a different definition from its parent class. What if User class didn’t have an is_admin flag but just checked if it had permission for something based on a permissions dictionary
# class User:
#   def __init__(self, username, permissions):
#     self.username = username
#     self.permissions = permissions
#
#   def has_permission_for(self, key):
#     if self.permissions.get(key):
#       return True
#     else:
#       return False
#
# class Admin(User):
#   def has_permission_for(self, key):
#     return True
# defined a class User which takes a permissions parameter in its constructor. Let’s assume permissions is a dict. User has a method .has_permission_for() implemented, where it checks to see if a given key is in its permissions dictionary
# define an Admin class that subclasses User. It has all methods, attributes, and functionality that User has. However, if you call has_permission_for on an instance of Admin, it won’t check its permissions dictionary. Since this User is also an Admin, we just say they have permission to see everything
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username

  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
  def edit_message(self, message, new_text):
    message.text =  new_text
#
# #---4/9 -- Super()
# add some extra logic to the existing method. super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on super()
# class Sink:
#   def __init__(self, basin, nozzle):
#     self.basin = basin
#     self.nozzle = nozzle
#
# class KitchenSink(Sink):
#   def __init__(self, basin, nozzle, trash_compactor=None):
#       #KitchenSink then calls the constructor for Sink with the basin and nozzle it received using the super() function, with this line of code
#       #call the constructor (the function called __init__) of the class that is this class’s parent class
#       super().__init__(basin, nozzle)
#     if trash_compactor:
#       self.trash_compactor = trash_compactor
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions, raisins=40):
    super().__init__(potatoes, celery, onions)
    if raisins:
      self.raisins = raisins
#---5/9 -- Interfaces
# interested in whether that object can perform a given task.
# class Chess:
#   def __init__(self):
#     self.board = setup_board()
#     self.pieces = add_chess_pieces()
#
#   def play(self):
#     print("Playing chess!")
#
# class Checkers:
#   def __init__(self):
#     self.board = setup_board()
#     self.pieces = add_checkers_pieces()
#
#   def play(self):
#     print("Playing checkers!")
#
# define two classes, Chess and Checkers. In Chess we define a constructor that sets up the board and pieces, and a .play() method
# have a play_game() function that takes an instance of Chess or Checkers, it could call the .play() method without having to check which class the object is an instance of
#
#
# def play_game(chess_or_checkers):
#   chess_or_checkers.play()
#
# chess_game = Chess()
# checkers_game = Checkers()
# chess_game_2 = Chess()
#
# for game in [chess_game, checkers_game, chess_game_2]:
#   play_game(game)
# """
# Prints out the following:
# Playing chess!
# Playing checkers!
# Playing chess!
# defined a play_game function that could take either a Chess object or a Checkers object. We instantiate a few objects and then call play_game on each
# two classes have the same method names and attributes, we say they implement the same interface
# An interface in Python usually refers to the names of the methods and the arguments they take
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
# Give VehicleInsurance a .get_rate() method that takes self as a parameter. Return .001 multiplied by the price of the vehicle
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001
# Give HomeInsurance a .get_rate() method that takes self as a parameter. Return .00005 multiplied by the price of the home
class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005

#---6/9 -- Polymorphism
# think of the + operator
# # For an int and an int, + returns an int
# 2 + 4 == 6
#
# # For a float and a float, + returns a float
# 3.1 + 2.1 == 5.2
#
# # For a string and a string, + returns a string
# "Is this " + "addition?" == "Is this addition?"
#
# # For a list and a list, + returns a list
# [1, 2] + [3, 4] == [1, 2, 3, 4]
# Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name) doing different actions depending on the type of data
# defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"
print(len(a_list))
print(len(a_dict))
print(len(a_string))

#---7/9--Dunder Methods
# define dunder methods that define a custom-made class to look and behave like a Python builtin
# class Color:
#   def __init__(self, red, blue, green):
#     self.red = red
#     self.blue = blue
#     self.green = green
#
#   def __repr__(self):
#     return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)
#
#   def add(self, other):
#     """
#     Adds two RGB colors together
#     Maximum value is 255
#     """
#     new_red = min(self.red + other.red, 255)
#     new_blue = min(self.blue + other.blue, 255)
#     new_green = min(self.green + other.green, 255)
#
#     return Color(new_red, new_blue, new_green)
#
# red = Color(255, 0, 0)
# blue = Color(0, 255, 0)
#
# magenta = red.add(blue)
# print(magenta)
# # Prints "Color with RGB = (255, 255, 0)"
# In this code we defined a Color class that implements an addition function. Unfortunately, red.add(blue) is a little verbose for something that we have an intuitive symbol for (i.e., the + symbol)
# Python offers the dunder method __add__ for this very reason
# rename the add() method above to something that looks like this
# class Color:
#   def __add__(self, other):
#     """
#     Adds two RGB colors together
#     Maximum value is 255
#     """
#     new_red = min(self.red + other.red, 255)
#     new_blue = min(self.blue + other.blue, 255)
#     new_green = min(self.green + other.green, 255)
#
#     return Color(new_red, new_blue, new_green)
# create the colors
# red = Color(255, 0, 0)
# blue = Color(0, 255, 0)
# green = Color(0, 0, 255)
# add them together using the + operator
# # Color with RGB: (255, 255, 0)
# magenta = red + blue
#
# # Color with RGB: (0, 255, 255)
# cyan = blue + green
#
# # Color with RGB: (255, 0, 255)
# yellow = red + green
#
# # Color with RGB: (255, 255, 255)
# white = red + blue + green
# we defined an __add__ method for our Color class, we were able to add these objects together using the + operator
class Atom:
  def __init__(self, label):
    self.label = label
  def __add__(self,other):
    return Molecule([self,other])

class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms

sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
#salt = sodium + chlorine

#---8/9 -- Dunder Methods II
# write functionality that allows custom defined types to behave like lists
# class UserGroup:
#   def __init__(self, users, permissions):
#     self.user_list = users
#     self.permissions = permissions
#
#   def __iter__(self):
#     return iter(self.user_list)
#
#   def __len__(self):
#     return len(self.user_list)
#
#   def __contains__(self, user):
#     return user in self.user_list
#
# __init__, our constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions when we create a new UserGroup
# __iter__, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax.
# __len__, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list
# __contains__, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have
# allow UserGroup to act like a list using syntax Python programmers will already be familiar with
# having syntax that allows for list-like operations can be very powerful
# use the following code to do this:
# class User:
#   def __init__(self, username):
#     self.username = username
#
# diana = User('diana')
# frank = User('frank')
# jenn = User('jenn')
#
# can_edit = UserGroup([diana, frank], {'can_edit_page': True})
# can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})
#
# print(len(can_edit))
# # Prints 2
#
# for user in can_edit:
#   print(user.username)
# # Prints "diana" and "frank"
#
# if frank in can_delete:
#   print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")
# created a set of users and then added them to UserGroups with specific permissions. Then we used Python built-in functions and syntax to calculate the length of a UserGroup, to iterate through a UserGroup and to check for a User‘s membership in a UserGroup
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
#Give LawFirm a .__len__() method that will return the number of lawyers in the law firm
  def __len__(self):
    return len(self.lawyers)
#Give LawFirm a .__contains__() method that takes two parameters: self and lawyer and checks to see if lawyer is in self.lawyers
  def __contains__(self, lawyer):
    return lawyer in self.lawyers
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

#---9/9--Review
class SortedList (list):
  def __init__(self,value):
    super().__init__(value)
    self.sort()

  def append(self, value):
    super().append(value)
    self.sort()
#    pass
lst = SortedList([4,1,5])
print(lst)
