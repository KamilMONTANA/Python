import turtle as t
import random

tim = t.Turtle()
tim.pensize(15)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()