import turtle

turtle.speed(100)


def draw_a_spiral(sidelength):
    for x in range(100):
        for x in range(3):
            turtle.forward(sidelength)
            turtle.left(90)
            sidelength=sidelength+1
    turtle.forward(sidelength)
    turtle.left(90)

draw_a_spiral(1)

turtle.exitonclick()
