#Ask for 5 items and calculate subtotal, then tax, then total
#2/22/2022
# CTI-110 P2HW1 - Total Purchases
#Jeremiah Grafals

#gets prices
item1 = float(input('Enter the price of item #1: ')) 
item2 = float(input('Enter the price of item #2: ')) 
item3 = float(input('Enter the price of item #3: ')) 
item4 = float(input('Enter the price of item #4: ')) 
item5 = float(input('Enter the price of item #5: ')) 

#calculations
subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * .07
total = subtotal + tax

#output
print('------Results------')
print("Subtotal: $", format(subtotal,',.2f'),sep='')
print("Sales Tax: $", format(tax,',.2f'),sep='')
print("Total with tax: $", format(total,',.2f'),sep='')
