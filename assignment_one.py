# Jack Fones
# 9-21-23
# this code creates 4 equal sized octagons, all of which are filled with a different color and are equally spaced.


# first we have to import the turtle thing
import turtle


#these lines make the pen look like a real turtle, as well as making it bigger and making it move backwards, for fun.
turtle.shape("turtle")
turtle.turtlesize(3)
turtle.tilt(180)

# these lines create a function that actually makes an octagon.
# the paramaters control the length of each line and the color of the octagon.
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


# each of these lines executes one of the two funtions.
# the parameters for the draw_an_octagon lines control the color and the size of the octagons,
# while the move_pen parameters have the x and y coordinates for the octagons.
# the octagons are all roughly 240 pixels wide,
# so they all start at variations of 250 so there are 10 pixels between each octagon.
# if you want to change the color, the size, or the location of the octagons you would edit those here.
draw_an_octagon("red", 100)
move_pen(0, 250)
draw_an_octagon("purple", 100)
move_pen(-250, 250)
draw_an_octagon("green", 100)
move_pen(-250, -0)
draw_an_octagon("blue", 100)

#i made the red octagon into a stop sign because i was bored
move_pen(-55,-165)
turtle.color("white")
turtle.write("STOP", align="left", font=('Arial',60,'bold'))

#the next 10 or so lines make a little diamond in the center because again, i was bored.
turtle.color("black")
move_pen(-4,4)
turtle.left(135)

turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

#this line hides the turtle so it's easier to see the octagons
turtle.hideturtle()

# this line keeps the window open so it doesn't close automatically after the octagons are done being drawn.
turtle.exitonclick()