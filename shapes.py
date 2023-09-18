
import turtle
turtle.speed(1000**100000)

turtle.penup()
turtle.forward(-350)
turtle.pendown()
for x in range(720):
    turtle.right(.5)
    for x in range(4):
        turtle.forward(200)
        turtle.right(90)

turtle.penup()
turtle.forward(700)
turtle.pendown()

for x in range(720):
    turtle.right(.5)
    for x in range(4):
        turtle.forward(200)
        turtle.right(90)

turtle.exitonclick()