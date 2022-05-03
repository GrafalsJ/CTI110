import turtle

i = 0   #creates the loop controller

#makes square
while i < 4:
    turtle.forward(150)
    turtle.right(90)
    i += 1

# I was going to move the triangle,
# but I decided to make a house instead
##turtle.forward(100)
##turtle.penup()
##turtle.pendown()

# Resets controller variable
i = 0

# Creates the triangle
while i < 3:
    turtle.forward(150)
    turtle.left(120)
    i += 1
    
