# เขียนแบบปกติ
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
        self.size = random.randint(1,100)
        self.name = str(random.random())
        self.pos = Vector(random.randint(1,500),random.randint(1,500))
        self.vel = Vector(random.randint(1,10),random.randint(1,10))
        self.acc = Vector(0,0.1)
        self.canvas = canvas
    
    def draw(self):
        self.canvas.create_oval(self.pos.x,self.pos.y,self.pos.x+self.size,self.pos.y+self.size , fill = "#%02x%02x%02x"%(self.R,self.G,self.B) , tag = self.name)
        
    def move(self):
        self.canvas.move(self.name,self.vel.x,self.vel.y)
        self.pos = self.pos + self.vel
        if self.pos.x<0:
            self.pos.x = 0
            self.vel.x *= -1
        if self.pos.y<0:
            self.pos.y = 0
            self.vel.y *= -1
        if self.pos.x > 500:
            self.pos.x = 500
            self.vel.x *= -1
        if self.pos.y > 500:
            self.pos.y = 500
            self.vel.y *= -1

class Tri():
    def __init__(self,canvas):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.size = random.randint(1,100)
        self.name = str(random.random())
        self.pos = Vector(random.randint(1,500),random.randint(1,500))
        self.vel = Vector(random.randint(1,10),random.randint(1,10))
        self.acc = Vector(0,0.1)
        self.canvas = canvas    

    def draw(self):
        self.canvas.create_polygon([self.pos.x,self.pos.y,self.pos.x+self.size,self.pos.y,self.pos.x+self.size,self.pos.y+self.size],fill = "#%02x%02x%02x"%(self.R,self.G,self.B) , tag = self.name)

    def move(self):
        self.canvas.move(self.name,self.vel.x,self.vel.y)
        self.pos = self.pos + self.vel
        if self.pos.x<0:
            self.pos.x = 0
            self.vel.x *= -1
        if self.pos.y<0:
            self.pos.y = 0
            self.vel.y *= -1
        if self.pos.x > 500:
            self.pos.x = 500
            self.vel.x *= -1
        if self.pos.y > 500:
            self.pos.y = 500
            self.vel.y *= -1

class Rect():
    def __init__(self,canvas):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.size = random.randint(1,100)
        self.name = str(random.random())
        self.pos = Vector(random.randint(1,500),random.randint(1,500))
        self.vel = Vector(random.randint(1,10),random.randint(1,10))
        self.acc = Vector(0,0.1)
        self.canvas = canvas    

    def draw(self):
        self.canvas.create_rectangle(self.pos.x,self.pos.y,self.pos.x+self.size,self.pos.y+self.size , fill = "#%02x%02x%02x"%(self.R,self.G,self.B) , tag = self.name)
        
    def move(self):
        self.canvas.move(self.name,self.vel.x,self.vel.y)
        self.pos = self.pos + self.vel
        if self.pos.x<0:
            self.pos.x = 0
            self.vel.x *= -1
        if self.pos.y<0:
            self.pos.y = 0
            self.vel.y *= -1
        if self.pos.x > 500:
            self.pos.x = 500
            self.vel.x *= -1
        if self.pos.y > 500:
            self.pos.y = 500
            self.vel.y *= -1

class Star():
    def __init__(self,canvas):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.size = random.randint(1,100)
        self.name = str(random.random())
        self.pos = Vector(random.randint(1,500),random.randint(1,500))
        self.vel = Vector(random.randint(1,10),random.randint(1,10))
        self.acc = Vector(0,0.1)
        self.canvas = canvas

    def draw(self):
        ps = []
        n = 5
        i = 0
        while i < n*2:
            ps.append(self.pos.x+self.size*math.cos(math.pi/n*i))
            ps.append(self.pos.x+self.size*math.sin(math.pi/n*i))
            i+=1
            ps.append(self.pos.x+self.size/2*math.cos(math.pi/n*i))
            ps.append(self.pos.x+self.size/2*math.sin(math.pi/n*i))
            i+=1
        self.canvas.create_polygon(ps , fill = "#%02x%02x%02x"%(self.R,self.G,self.B) , tag = self.name)

    def move(self):
        self.canvas.move(self.name,self.vel.x,self.vel.y)
        self.pos = self.pos + self.vel
        if self.pos.x<0:
            self.pos.x = 0
            self.vel.x *= -1
        if self.pos.y<0:
            self.pos.y = 0
            self.vel.y *= -1
        if self.pos.x > 500:
            self.pos.x = 500
            self.vel.x *= -1
        if self.pos.y > 500:
            self.pos.y = 500
            self.vel.y *= -1

window = Tk()
canvas = Canvas(window,width=500,height=500)
canvas.pack()

bs = []
ts = []
rs = []
ss = []

for i in range(0,10):
    bs.append(Ball(canvas))
    bs[-1].draw()
for i in range(0,10):
    ts.append(Tri(canvas))
    ts[-1].draw()
for i in range(0,10):
    rs.append(Rect(canvas))
    rs[-1].draw()
for i in range(0,10):
    ss.append(Star(canvas))
    ss[-1].draw()

while True:
    for i in range(0,len(bs)):
        bs[i].move()
    for i in range(0,len(ts)):
        ts[i].move()        
    for i in range(0,len(rs)):
        rs[i].move()
    for i in range(0,len(ss)):
        ss[i].move()
    canvas.after(20)
    canvas.update()
window.mainloop()         