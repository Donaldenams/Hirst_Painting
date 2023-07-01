import turtle

import colorgram
from turtle import Turtle, Screen
import random

dee = Turtle()
colors = colorgram.extract('twohirsts.jpg', 30)
turtle.colormode(255)
dee.speed('fastest')

def extract_color():
    rgb_colors = []
    for x in colors:
        r = x.rgb.r
        g = x.rgb.g
        b = x.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)


color_list = [(165, 52, 81), (218, 154, 100), (43, 96, 148), (119, 162, 197), (57, 124, 61), (166, 25, 46),
              (204, 78, 102), (130, 190, 162), (25, 56, 131), (158, 83, 50), (211, 157, 27), (218, 84, 58),
              (229, 200, 94), (200, 138, 165), (53, 165, 110), (22, 47, 87), (56, 38, 45), (29, 90, 43),
              (214, 178, 201), (20, 71, 39), (171, 191, 220), (159, 204, 216), (235, 201, 3), (165, 207, 188),
              (112, 120, 162), (154, 32, 29)]


dee.setheading(225)
dee.penup()
dee.fd(300)
dee.setheading(0)


dot_numbers = 100


for x in range(1, dot_numbers):
    dee.dot(12, random.choice(color_list))
    dee.penup()
    dee.fd(50)
    if x % 10 == 0:
        dee.setheading(90)
        dee.fd(50)
        dee.setheading(180)
        dee.fd(500)
        dee.setheading(0)





see = Screen()
see.exitonclick()
