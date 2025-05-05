import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.pensize(2)
t.pencolor("cyan")
t.speed(0)

for i in range(36):
    for j in range(4):
        t.circle(100)
        t.left(90)
    t.left(10)

turtle.done()
