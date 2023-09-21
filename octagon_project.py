import turtle

def draw_an_octogon(color,size):
    turtle.begin_fill()
    for x in range(8):
        turtle.color(color)
        turtle.forward(size)
        turtle.right(45)
    turtle.end_fill()

def move_pen(x_coordinate,y_coordinate):
    turtle.penup()
    turtle.goto(x_coordinate,y_coordinate)
    turtle.pendown()


draw_an_octogon("blue",100)
move_pen()
draw_an_octogon("red", 100)
move_pen()
draw_an_octogon("yellow", 100)
move_pen()
draw_an_octogon("pink", 100)
move_pen()
turtle.exitonclick()