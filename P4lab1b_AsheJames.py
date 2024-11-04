# James Ashe
# 11-3-2024
# Initials

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.color("red")
pen.pensize(5)

# Function to draw the letter J
def draw_J():
    pen.penup()
    pen.goto(-50, 0)  # Starting point for J
    pen.pendown()
    pen.right(90)      # Face down
    pen.circle(25, 180)  # Draw a semicircle
    pen.forward(50)       # Draw the horizontal line

# Function to draw the letter "A"
def draw_a():
    pen.penup()
    pen.goto(-20, 0)  # Starting point for "a"
    pen.pendown()
    
    # Draw the circle part of "a"
    pen.circle(20)  # Draw a circle with radius 20
    
    pen.right(90)   # Turn to face downwards
    pen.forward(40) # Draw the vertical line of "a"
    
    pen.left(90)    # Turn to face right
    pen.forward(10) # Move to the right for the crossbar of "a"
    
    pen.right(90)   # Face downwards again
    pen.forward(20) # Draw the crossbar of "a"
    
    pen.penup()

# Draw the initials
draw_J()
draw_A()

# Hide the turtle and finish
pen.hideturtle()
turtle.done()

