#Functions
#define
def functionname():
#add things to do tabbed or indented 2 / 4 spaces
  print("my message here")

#variables inside functions
def function(variable):
  print ("same shit different" + variable)
#call function with variable
function(day)

#multi variable inside functions:
def function(v1,v2,v3):
  print (" This is variable one: " + v1)
  print (" This is variable two: " + v2)
  print (" This is variable three: " + v3)

function(boots,shoes,coat)

#if no variable is assigned during the call it searches for a prior assigned variable
variable = day
#way later in the code
def function():
  print ("same shit different " + variable)

#able to set default in the function call itself
def function(variable="day"):
#can not start with a default set, and then list changing needs to be the opposite
# as open ended first, then positionally
# not correct way of setting default in a function
def function (item1="boots",item2,item3):
  print (item1,item2,item3)
function (shoes,coat)
#correct way of setting default in a function
def function (item1,item2,item3="coat"):
  print (item1,item2,item3)
function (boots,shoes)

---
# Define create_spreadsheet():
def create_spreadsheet(title,row_count="1000"):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows.")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")

#to define variables in call
# Define create_spreadsheet():
def create_spreadsheet(title,row_count):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows.")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Applications","10")

----
#returned function value computational
#FollowAlong
def divide_by_four(input_number):
    return input_number/4
result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")

#returned function value with strings
def create_special_string(special_item):
    return "Our special is " + special_item + "."

special_string = create_special_string("banana yogurt")

print(special_string)

#exercise
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
my_age = calculate_age(2049,1993)
dads_age = calculate_age(2049,1953)

#Multiple return Values
#FollowAlong
def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
x_squared, y_squared = square_point(1, 3) # where you call the function with new variables
print(x_squared)
print(y_squared)

#exercise
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit
#assign two new variables to the first variables (in order)low_limit, high_limit
#with the function call
low, high = get_boundaries(100,20)

---
#Scope - creating variable accessible outside the function
#FollowAlong
def create_special_string(special_item):
    return "Our special is " + special_item + "."
print("I don't like " + special_item) # wont work as special_item is not defined

header_string = "Our special is "  #defined outside the function

def create_special_string(special_item):
    return header_string + special_item + "." # called in the function - works
print(create_special_string("grapes"))

#Review:
def repeat_stuff(stuff,num_repeats=10): #created func, had 1 positional 1 default variable
return stuff*num_repeats
lyrics = repeat_stuff("Row ",3) + "Your Boat. " #inside function called row 3 times then your boat
song = repeat_stuff(lyrics) #called the variable above 10 times (default was set to 10)
print(song)
