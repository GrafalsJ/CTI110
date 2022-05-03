#this was the closest I could get to a snowflake
#3-18-2022


import turtle

turtle.right(35)
turtle.hideturtle()

#Big square
for i in range(4):
    turtle.forward(150)
    turtle.right(90)
turtle.left(90)

#small squares 1
for i in range(6):
    turtle.forward(100)
    turtle.left(90)
turtle.right(90)
for i in range(4):
    turtle.forward(50)
    turtle.right(90)

#move to next area
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)

#small squares 2
for i in range(6):
    turtle.forward(100)
    turtle.right(90)
turtle.left(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

#move to next area
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.forward(150)

#small squares 3
for i in range(6):
    turtle.forward(100)
    turtle.right(90)
turtle.left(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

#move to next area
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.forward(150)

#small squares 4
for i in range(6):
    turtle.forward(100)
    turtle.right(90)
turtle.left(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

