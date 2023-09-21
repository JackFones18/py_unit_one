import turtle

def draw_an_octogon(color,size):
    turtle.begin_fill()
    for x in range(8):
        turtle.color(color)
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()

draw_an_octogon("blue",100)
draw_an_octogon("red", 50)
draw_an_octogon("yellow", 200)
turtle.exitonclick()