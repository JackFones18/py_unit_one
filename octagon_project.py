import turtle

def draw_an_octogon(color,size):

    for x in range(8):
        turtle.color(color)
        turtle.forward(size)
        turtle.right(45)

draw_an_octogon(blue,100)
turtle.exitonclick()