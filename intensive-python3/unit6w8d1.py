#---1/14 -- Types
# 1.Call type() on the integer 5 and print the results.
# 2.# Define a dictionary my_dict.
# 3.# Print out the type() of my_dict.
# 4.# Define a list called my_list.
# 5.# Print out the type() of my_list.
int=4
print(type(int))
my_dict={}
print(type(my_dict))
my_list=[]
print(type(my_list))

#---2/14 -- class
#class is a template for a data type
# class CoolClass:
#   pass
class Facade:
  pass
#---3/14 -- Instantiation
#Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined CoolClass as follows
#cool_instance = CoolClass()
class Facade:
  pass
  #Make a Facade instance and save it to the variable facade_1
facade_1 = Facade()
#---4/14 -- Object Oriented Programming
# class instance is also called an object. pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming
# print(type(cool_instance))
# prints "<class '__main__.CoolClass'>"
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

#---5/14 -- Class Variables
#A class variable is a variable that’s the same for every instance of the class..including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax
# class Musician:           #defined the class Musician
#   title = "Rockstar"      #becomes .title of musician() (class attribute)
#
# drummer = Musician()      #instantiated drummer to be an object of type Musician
# print(drummer.title)      #printed out the drummer’s .title attribute
# # prints "Rockstar"
class Grade:
  minimum_passing = 65
print(Grade.minimum_passing)

#---6/14 -- Methods
# functions that are defined as part of a class.argument in a method is always the object that is calling the method.
# define methods similarly to functions, except that they are indented to be part of the class
# class Dog():                  #Class
#   dog_time_dilation = 7       #Class variable
#
#   def time_explanation(self): #start of method
#     print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))
#
# pipi_pitbull = Dog()          #calling the class as a new variable
# pipi_pitbull.time_explanation()   #calling with the method defined under the class (uses self)
# # Prints "Dogs experience 7 years for every 1 human year."
class Rules():
  def washing_brushes(self):
    return("Point bristles towards the basin while washing your brushes.")
rules_class= Rules()
rules_class.washing_brushes()

#---7/14 -- Methods with arguments
#Methods can also take more arguments than just self
# class DistanceConverter:      #defined a DistanceConverter class,
#   kms_in_a_mile = 1.609
#   def how_many_kms(self, miles):  #self is implicitly passed (and refers to the object converter)
#     return miles * self.kms_in_a_mile
#
# converter = DistanceConverter()   #instantiated it
# kms_in_5_miles = converter.how_many_kms(5)
# print(kms_in_5_miles)
# # prints "8.045"
class Circle():
  pi = 3.14
  def area(self, radius):
    area = Circle.pi * (radius/2)  ** 2
    return area
circle = Circle()

pizza_area = circle.area(12)
print(pizza_area)
teaching_table_area = circle.area(36)
print(teaching_table_area)
round_room_area= circle.area(11460)
print(round_room_area)

#---8/10 -- Constructors
# Several methods that we can define in a Python class that have special behavior.
# Another popular term is dunder methods.have two underscores (double-underscore abbreviated to “dunder”)
# __init__  - initialize a newly created object. Methods that are used to prepare an object being instantiated are called constructors.
# class Shouter:
#   def __init__(self, phrase):
#     # make sure phrase is a string
#     if type(phrase) == str:
#
#       # then shout it out
#       print(phrase.upper())
#
# shout1 = Shouter("shout")
# # prints "SHOUT"
#
# shout2 = Shouter("shout")
# # prints "SHOUT"
#
# shout3 = Shouter("let it all out")
# # prints "LET IT ALL OUT"
class Circle:
  pi = 3.14
  def __init__(self,diameter):
  # Add constructor here:
  	print(str("New circle with diameter: " + diameter))
teaching_table = Circle("36")

#---9/10 -- Instance variables
# data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to

class Store:
  pass
alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#---10/14 -- Attribute functions
#attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError
# class NoCustomAttributes:
#   pass
#
# attributeless = NoCustomAttributes()
#
# try:
#   attributeless.fake_attribute
# except AttributeError:
#   print("This text gets printed!")
#
# # prints "This text gets printed!"
# getattr() is a Python function that works a lot like the usual dot-syntax (i.e., object_name.attribute_name) but we can supply a third argument that will be the default if the object does not have the given attribute
# hasattr() will return True if an object has a given attribute and False otherwise
# hasattr(attributeless, "fake_attribute")
# # returns False
#
# getattr(attributeless, "other_fake_attribute", 800)
# # returns 800, the default value
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for i in how_many_s:
  if hasattr(i,"count"):
    print(i.count("s"))

#--- 11/14 -- self
# class SearchEngineEntry:
#   def __init__(self, url):
#     self.url = url
#
# codecademy = SearchEngineEntry("www.codecademy.com")
# wikipedia = SearchEngineEntry("www.wikipedia.org")
#
# print(codecademy.url)
# # prints "www.codecademy.com"
#
# print(wikipedia.url)
# # prints "www.wikipedia.org"

# class SearchEngineEntry:
#   secure_prefix = "https://"
#   def __init__(self, url):
#     self.url = url
#
#   def secure(self):
#     return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
#
# codecademy = SearchEngineEntry("www.codecademy.com")
#
# print(codecademy.secure())
# # prints "https://www.codecademy.com"
#
# print(wikipedia.secure())
# # prints "https://www.wikipedia.org"
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = (diameter/2)
  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#---12/14 Everything is an object
# fun_list = [10, "string", {'abc': True}]
#
# type(fun_list)
# # Prints <class 'list'>
#
# dir(fun_list)
# # Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir(5)
def this_function_is_an_object(obj):
  return obj
print(dir(this_function_is_an_object))

#---13/14 Representation
# another dunder method called __repr__. This is a method we can use to tell Python what we want the string representation of the class to be. __repr__ can only have one parameter, self, and must return a string.
# class Employee():
#   def __init__(self, name):
#     self.name = name
#
#   def __repr__(self):
#     return self.name
#
# argus = Employee("Argus Filch")
# print(argus)
# # prints "Argus Filch"
class Circle:
  pi = 3.14

  def __init__(self, diameter):
    self.radius = diameter / 2

  def area(self):
    return self.pi * self.radius ** 2

  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza)
print(teaching_table)
print(round_room)

#--- 14/14 -- Review
class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = list()

  def add_grade(self,grade):
    if type(grade) == Grade:
      self.grades.append(grade)

  def get_average(self):
    average=self.grade.mean()
    return average

class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score
  def is_passing(self):
    if self.score > self.minimum_passing:
      return "Passing grade!"
    else:
      return "Not Passing."
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

new_grade = Grade(100)
pieter.add_grade(new_grade)
