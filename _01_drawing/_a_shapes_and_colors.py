import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    my = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    my.shape('turtle')
    # Set your turtle's speed using .speed(2)
    my.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    my.color('green')
    my.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range(4):
        my.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        my.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    # yes
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    my.goto(100, 100)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    my.begin_fill()
    my.circle(55, 365)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    my.end_fill()
    # Draw 3 more shapes with different fill colors!
    my.goto(1, 1)
    my.begin_fill()
    my.circle(55, 182)
    my.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
