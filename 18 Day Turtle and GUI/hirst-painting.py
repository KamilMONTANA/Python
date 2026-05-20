""" Code for extracting colors from the image
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

import turtle as t
import random


t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed('fastest')
tim.hideturtle()

x = -450
y = -350
for _ in range(19):
    tim.setx(x)
    tim.sety(y)
    y = y + 50
    for _ in range(19):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


screen = t.Screen()
screen.exitonclick()