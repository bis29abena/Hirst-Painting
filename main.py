# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
# r = color.rgb.r
# g = color.rgb.g
# b = color.rgb.b
# new_color = (r, g, b)
# rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen

# Getting a list of colors in an r g b form which will be used for our hirst painting
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]

# Creating an object called hirst for the class Turtle
hirst = Turtle()
# Creating an object called screen for the class screen
screen = Screen()
# A method in the turtle class which enables us to use the rgb color encoding in our canvas
turtle.colormode(255)
# Hiding our turtle
hirst.hideturtle()
# Taking the height and width of canvas
h = screen.canvheight / 2
w = screen.canvwidth / 2
# Using the difference of the height and width for our horizontal spacing
h_w_spacing = w - h
# This loop takes care of the upward movement
# it moves up 10x
# set the starting position of our turtle
for _ in range(10):
    hirst.penup()
    hirst.setx(-w)
    hirst.sety(-h)
    # Forward movement of the turtle
    # Moves 10x to the right
    # having a spacing of 50 paces in between
    for _ in range(10):
        hirst.dot(20, random.choice(color_list))
        hirst.penup()
        hirst.forward(50)
    h -= h_w_spacing - 10

screen.exitonclick()
