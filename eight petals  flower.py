import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.pensize(2)
t.pencolor("magenta")

def petal():
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)

for _ in range(8):
    petal()
    t.left(45)

turtle.done()
