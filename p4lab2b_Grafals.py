import turtle

turtle.pencolor('#009933')  #Green
turtle.right(90)
turtle.forward(50)
i = 0

#Initial curve
while i < 18:
    turtle.right(10)
    turtle.forward(5)
    i+= 1

turtle.penup()    
turtle.right(180)
i = 0

#Goes back across curve
while i < 18:
    turtle.left(10)
    turtle.forward(5)
    i+= 1

turtle.pendown()

turtle.forward(60)

turtle.left(90)
turtle.forward(30)
turtle.right(180)
turtle.forward(60)

turtle.penup()

turtle.forward(100)

turtle.right(180)

turtle.pendown()

turtle.pencolor('#ff0000')  #Red
i = 0

#makes G
while i < 27:
    turtle.left(10)
    turtle.forward(9)
    i+= 1

#Straight part of G    
turtle.left(90)
turtle.forward(30)
turtle.right(180)
turtle.forward(55)
turtle.right(90)
turtle.forward(50)
