import turtle


def draw_an_octagon(color, size):
    turtle.begin_fill()
    for x in range(8):
        turtle.color(color)
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()


def move_pen(x_coordinate, y_coordinate):
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()


draw_an_octagon("red", 100)
move_pen(0, 250)
draw_an_octagon("gold", 100)
move_pen(-250, 250)
draw_an_octagon("green", 100)
move_pen(-250, -0)
draw_an_octagon("blue", 100)
turtle.exitonclick()
