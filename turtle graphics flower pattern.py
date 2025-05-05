import turtle

screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.pencolor("yellow")
pen.speed(10)

for i in range(72):
    pen.circle(100)
    pen.left(5)

pen.hideturtle()
screen.mainloop()

