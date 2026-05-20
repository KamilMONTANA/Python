import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.listen()

screen.onkey(key="w", fun=lambda: tim.forward(10))
screen.onkey(key="s", fun=lambda: tim.backward(10))
screen.onkey(key="a", fun=lambda: tim.left(10))
screen.onkey(key="d", fun=lambda: tim.right(10))

screen.onkey(key="c", fun=lambda: tim.reset())

screen.exitonclick()
