import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

h = 0
n = 36
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.forward(i * 3 / n + i)
    t.left(60)
    h += 0.005

turtle.done()
