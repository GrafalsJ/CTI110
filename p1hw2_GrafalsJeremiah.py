# Pizza Order Calculator
#   Must multiply students by 3 for number of slices per kid
#   Must divide students by 2 since 1 pizza for 2 kids

# 2/10/2022
# CTI-110 P1HW2 - Pizza Order
# Jeremiah Grafals Quinones
#

students = int(input("How many students do you want to order pizza for? "))

slicesneeded = students* 3
print("Pizza Slices Needed: ", slicesneeded)

pizzasneeded = float(students/2)
print("Pizzas needed: ", pizzasneeded)
