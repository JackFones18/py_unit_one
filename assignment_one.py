# Jack Fones
#9-21-23
# this code creates 4 equal sized octagons, all of which are filled with a differenct color and are equally spaced.


# first we have to import the turtle thing
import turtle


#these lines create a function that actually makes an octagon. the paramaters control the length of each line and the color of the octagon.
def draw_an_octagon(color, size):
    turtle.begin_fill()
    turtle.color(color)
    for x in range(8):
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()


# these lines crate a funtion that moves the pen to the next coordinate. This decides where the next octagon will be.
def move_pen(x_coordinate, y_coordinate):
    turtle.penup()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.pendown()


# each of these lines executes one of the two funtions. the parameters for the draw_an_octagon lines control the color and the size of the octagons, while the move_pen parameters have the x and y coordinates for the octagons.
# the octagons are all roughly 240 pixels wide, so they all start at variations of 250 so there are 10 pixels between each octagon.
draw_an_octagon("red", 100)
move_pen(0, 250)
draw_an_octagon("gold", 100)
move_pen(-250, 250)
draw_an_octagon("green", 100)
move_pen(-250, -0)
draw_an_octagon("blue", 100)

#this line keeps the window open so it doesnt close automatically after the octagons are done being drawn.
turtle.exitonclick()
