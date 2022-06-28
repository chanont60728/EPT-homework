import math
import random
from tkinter import *

class Vector():
    x=0.0
    y=0.0
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,v):
        return Vector(self.x+v.x,self.y+v.y)
    def __sub__(self,v):
        return Vector(self.x-v.x,self.y-v.y)
    def __mul__(self,m):
        return Vector(self.x*m,self.y*m)
    def dot(self,v):
        return (self.x*v.x)+(self.y*v.y)
    def size(self):
        return math.sqrt(self.x**2+self.y**2)
    def unit(self):
        s=self.size(self)
        return Vector(self.x/s , self.y/s)
    
class Ball():
    def __init__(self,canvas):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.size = 20
        self.name = str(random.random())
        self.pos = Vector(random.randint(1,200),random.randint(1,200)+250)
        self.vel = Vector(random.randint(10,20),10)
        self.canvas = canvas
    
    def draw(self):
        self.canvas.create_oval(self.pos.x,self.pos.y,self.pos.x+self.size,self.pos.y+self.size , fill = "#%02x%02x%02x"%(self.R,self.G,self.B) , tag = self.name)
        
    def move(self):
        self.pos = self.pos + self.vel
        if self.pos.x-self.size<=0:
            self.pos.x = 0 + self.size
            self.vel.x *= -1
        if self.pos.y-self.size<=0:
            self.pos.y = 0 + self.size
            self.vel.y *= -1
        if self.pos.x + self.size >= 800:
            self.pos.x = 800-self.size
            self.vel.x *= -1
        if self.pos.y +self.size >= 500:
            self.pos.y = 500 - self.size
            self.vel.y *= -1
        self.canvas.move(self.name,self.vel.x,self.vel.y)

class Bar():
    isDead = False

    def __init__(self,canvas,x,y):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.w = 150
        self.h = 20
        self.name = str(random.random())
        self.pos = Vector(x,y)
        self.canvas = canvas

    def draw(self):
        self.canvas.create_rectangle(self.pos.x,self.pos.y,self.pos.x+self.w,self.pos.y+self.h,fill = "#%02x%02x%02x"%(self.R,self.G,self.B) , tag = self.name)

    def isCollision(self,b):
        if (b.pos.x - b.size <= self.pos.x +self.w) and (b.pos.x - b.size >= self.pos.x) and (b.pos.y-b.size <= self.pos.y+self.h) and (b.pos.y-b.size>=self.pos.y):
            return True
        return False

    def dead(self):
        self.isDead = True
        self.canvas.delete(self.name)

window = Tk()
canvas = Canvas(window,width=800,height=500)
canvas.pack()

ball = Ball(canvas)
ball.draw()
bars=[]

for i in range(0,5):
    bars_tmp = []
    for j in range(0,5):
        bars_tmp.append(Bar(canvas,j*152+20,i*22+20))
        bars_tmp[j].draw()
    bars.append(bars_tmp)

while True:
    for i in range(0,len(bars)):
        for j in range(0,len(bars[0])):
            if not bars[i][j].isDead and bars[i][j].isCollision(ball):
                bars[i][j].dead()
                ball.vel.y *= -1
    ball.move()
    canvas.after(20)
    canvas.update() 

window.mainloop()         