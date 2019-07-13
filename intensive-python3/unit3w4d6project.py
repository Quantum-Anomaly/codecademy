#!/usr/bin/env python3
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
#figure out how many pizzas you sell
print("we sell " + str(num_pizzas) + " different kinds of pizza!")
#combine into one list with the prices attached to the slice
pizzas = list(zip(prices,toppings))
print(pizzas)
#here is the sorting magic
sorted_pizzas = sorted(pizzas)
print(sorted_pizzas)
#cheapest pizza
cheapest_pizza = sorted_pizzas[0]
#most expensive pizza
priciest_pizza = sorted_pizzas[-1]
#three of the cheapest
three_cheapest = sorted_pizzas [:3]
print(three_cheapest)
#how many 2 dollar items are there?
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
