hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0
haircut_sale = []

#Total of all the haircut costs
total_price = sum(prices)
#Find out the average price of a haircut is
average_price = total_price/len(prices)
print("Average Haircut Price: $" + str(average_price) + '\n')
#reduce haircut prices by $5
new_prices = [oldp-5 for oldp in prices]
print("New haircut prices: "'\n' + str(new_prices) + '\n')
#Get total revenue (prices list *last week list)
for i in range(len(hairstyles)):
  total_revenue += (prices[i]*last_week[i])
print("Total Revenue: $" + str(total_revenue) + '\n')
#find average daily revenue
average_daily_revenue = total_revenue / 7
print("Your average daily revenue stream: $" + str((average_daily_revenue))+'\n')
#advertise haircuts that are under $30
styles_prices = sorted(list(zip(new_prices,hairstyles)))
for i in range(len(styles_prices)):
  if styles_prices[i][0] < 30:  #important selecting list element and element index list[element][indexofelement]
    haircut_sale += [styles_prices[i]] # change this to [styles_prices[i][1]] to only print the names of the haircuts without the cost
print("Haircuts under $30: " '\n' + str(haircut_sale))
