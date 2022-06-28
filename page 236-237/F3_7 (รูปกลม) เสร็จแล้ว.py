import turtle 
t = turtle.Turtle()
radius = 100
t.speed(10)
t.penup()
t.right(90)
t.forward(radius)
t.left(90)
t.pendown()

t.circle(radius)

t.penup()
t.right(-90)
t.forward(radius)
t.left(-90)
t.pendown()

t.backward(radius)
i = 0
while i<=90:
    t.forward(radius)
    t.right(25)
    t.backward(radius)
    i=i+1
t.forward(radius)
t.left(25)
t.forward(200)
turtle.mainloop()

