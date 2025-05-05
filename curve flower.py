import turtle
import math

t = turtle.Turtle()
turtle.bgcolor("black")
t.pencolor("red")
t.speed(0)

for theta in range(3600):
    r = 200 * math.sin(4 * math.radians(theta))
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    t.goto(x, y)

turtle.done()
