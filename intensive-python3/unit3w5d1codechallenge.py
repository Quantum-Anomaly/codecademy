#!/usr/bin/env python3
#---
#2/11 - DoubleIndex
#Write your function here
def double_index(lst,index):
  # the range of spots in list in example go from 0-3 so an index of 4 is invalid, this checks to make sure the index is less than len of the lst
  if index <= len(lst):
    #in list find index and multiply that spot by 2 and change the original list to include the new value
    lst[index] = lst[index] * 2
      #If index is not a valid index, the function should return the original list.
return lst
#Uncomment the line below when your function is done
#this index has 4 spots
#2 is the spot or (index) of lst (0,1,2,3) which the value of is -10
print(double_index([3, 8, -10, 12], 2))

#---
#3/11 - Remove middle
#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#---
#4/11 - More than n
#Write your function here
def more_than_n(lst,item,n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#---
#5/11 - More frequent items
#Write your function here
def more_frequent_item(lst,item1,item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#---
#6/11 - Middle item
#Write your function here
def middle_element(lst):
  #checks to see if even by not having a remainder
  if len(lst)%2 == 0: #returns even numbers ==1 returns odd
    return (lst[(int(len(lst)/2))] + lst[(int(len(lst)/2) - 1)])/2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -10, -4, 4]))

#---
#7/11 - Append Sum
#Write your function here
def append_sum(lst):
  for i in range(0,3):
    lst.append(sum(lst[-2:]))
  return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#---
#8/11 - Larger list
#Write your function here
def larger_list(lst1,lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#---
#9/11 - Combine sort
#Write your function here
def combine_sort(lst1,lst2):
  #adds the lists together forming one new list with all numbers separate
  add_lst = lst1 + lst2
  return sorted(list(add_lst))
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

def combine_sort(lst1,lst2):
  #keep list indices together and combine
  new_lst =list(zip(lst1,lst2))
  return sorted(new_lst)
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#---
#10/11 - append size
#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#---
#11/11 - Every three nums
#Write your function here
def every_three_nums(start):
  if start > 100:
    return list()
  else:
    return list(range(start,101,3))


#Uncomment the line below when your function is done
print(every_three_nums(91))

#---
