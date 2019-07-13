set_to_true = True
set_to_false = False
#set a variable equal to a boolean
bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
#once set, returns either true or false
>>>bool_three
True
>>>bool_four
False
>>>bool_five
True
---
4/13 - Booleans
my_baby_bool = "true"
my_baby_bool_two = True
print(type(my_baby_bool))
print(type(my_baby_bool_two))
---
5/13 - If statements
def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"

# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

print(dave_check(user_name)) #called dave check with the username variable passed in
---
6/13 Relational Operators 2
#works
def greater_than(x,y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return "These numbers are the same"
#also works
def greater_than(x,y):
  max(x,y)
  if x == y:
    return "These numbers are the same"
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
print(graduation_reqs(120))
---
7/13 Boolean Opeartors - And
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
def graduation_reqs(gpa,credits):
  if credits >= 120 and gpa >=2.0:
    return "You meet the requirements to graduate!"
  else:
    return "You do not meet the requirements to graduate"
print(graduation_reqs(1.5,120))
---
8/13 Boolean Operators - Or
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
def graduation_mailer(gpa,credits):
  if gpa >= 2.0 or credits >= 120:
    return True
print(graduation_mailer(1.4,133))
---
9/13 Boolean Operators - Not
statement_one =not (4 + 5 <= 9)

statement_two =not (8 * 2) != 20 - 4

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 2.0) and (credits >=120):
    return "Your GPA is not high enough to graduate."
  if (gpa < 2.0) and (credits < 120):
    return "You do not meet either requirement to graduate!"
print(graduation_reqs(1.4,119))
---
10/13 Else Statements
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."
  print(graduation_reqs(1.1,101))
  ---
  11/13 Else If statements
  grade = ""
def grade_converter(gpa):
  if gpa >= 4.0:
    grade = "A"
  elif gpa >= 3.0:
    grade = "B"
  elif gpa >=2.0:
    grade = "C"
  elif gpa >=1.0:
    grade = "D"
  else:
    grade = "F"
  return grade
print(grade_converter(4.22))
---
12/13 - Try and Except

def raises_value_error():
  raise ValueError
try:
  raises_value_error()		#What you know that may cause this to error out
except ValueError:				#What type of error are you expecting
  print ("You raised a ValueError!")
---
13/13 - Review
def applicant_selector(gpa,ps_score,ec_count):
  if gpa >=3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >=3.0 and ps_score >= 90 and ec_count < 3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."
print(applicant_selector(3.2,99,4))
