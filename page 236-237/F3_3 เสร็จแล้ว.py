import turtle
import time

s = turtle.getscreen()
turtle.title("การบ้านคั่นเวลา")
t = turtle.Turtle()
t.pencolor("red")
t.pen(fillcolor="blue")

# ยกปากกาไปไว้ซ้ายบน
t.penup()
t.backward(100)
t.left(90)
t.forward(100)
t.right(90)
t.pendown()

# วาดสี่เหลี่ยม
t.begin_fill()
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

# ยกปากกาไปทางขวาบน
t.penup()
t.forward(200)
t.right(90)
t.forward(50)
t.pendown()

# วาดวงกลม
t.pen(fillcolor="yellow")
t.begin_fill()
t.circle(50)
t.end_fill()


# ยกปากกาลงขวาล่าง
t.penup()
t.forward(200)
t.pendown()

# วาดสามเหลี่ยม
t.pen(fillcolor="green")
t.begin_fill()
t.left(90)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

# ยกปากกาไปซ้ายล่าง
t.penup()
t.right(60)
t.forward(250)
t.pendown()

# วาดดาว
t.pen(fillcolor="gray")
t.begin_fill()
for i in range(5):
    t.right(145)
    t.forward(80)
t.end_fill()

# รอ 3 วินาทีเพื่อ reset หน้าจอ
time.sleep(3)
t.reset()

# วาดรูปปลา (มั้ง)
t.penup()
t.backward(50)
t.pendown()
t.left(40)
t.speed(20)
t.pen(fillcolor="yellow")
t.begin_fill()
for i in range(80):
    t.forward(2)
    t.right(1)
t.left(100)
for i in range(50):
    t.forward(2)
    t.right(1)
t.right(160)
for i in range(80):
    t.forward(1.7)
    t.left(1)
t.right(160)
for i in range(30):
    t.forward(1.7)
    t.left(1)
t.left(50)
for i in range(80):
    t.forward(2)
    t.right(1)
t.end_fill()
t.penup()
t.goto(30,30)
t.pendown()
t.right(70)
t.pen(fillcolor="yellow")
t.begin_fill()
for i in range(50):
    t.forward(2)
    t.right(1)
t.right(160)
for i in range(51):
    t.forward(1.7)
    t.left(1)
t.end_fill()
t.penup()
t.goto(30,-47)
t.pendown()
t.pen(fillcolor="yellow")
t.begin_fill()
for i in range(40):
    t.forward(2)
    t.left(1)
t.right(160)
for i in range(55):
    t.forward(1.7)
    t.right(1)
t.end_fill()
t.penup()
t.goto(0,10)
t.pendown()
t.pen(fillcolor="black")
t.begin_fill()
t.circle(5)
t.end_fill()

turtle.hideturtle()
turtle.mainloop()