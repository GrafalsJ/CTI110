# Pizza Order Calculator
#   Must multiply students by 3 for number of slices per kid
#   Must divide students by 2 since 1 pizza for 2 kids

# 2/10/2022
# CTI-110 P1HW2 - Pizza Order
# Jeremiah Grafals Quinones
#
def main():
    students = int(input("How many students do you want to order pizza for? "))
    peopleperpizza = int(input('Enter number of people per pizza (1.5, 2, or 3): '))

    if (peopleperpizza != 1.5) and (peopleperpizza != 2) and (peopleperpizza != 3):
        print('INVALID ENTRY!!!! \nShould have entered 1.5, 2, or 3')
        print('Run program again')
    else:
        print('----Pizza Order----')
        
        #prints student count
        print('Number of students:', students)
        
        #calcs pizzas needed
        #Determines if extra pie is needed
        if (students % peopleperpizza) > 0:
            pizzasneeded = float(students/peopleperpizza)+1
        else:
            pizzasneeded = students/peopleperpizza
            
        print("Pizzas needed:", format(pizzasneeded,'.0f'))
        
        #calcs price
        subtotal = 5 * pizzasneeded
        tax = subtotal * .06
        total = subtotal + tax
        print('Price: $',format(total,'.2f'),sep='')
        
main()
