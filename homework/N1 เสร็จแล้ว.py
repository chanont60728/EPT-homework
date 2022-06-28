import random
from graphics import *

class Vector():
    def __init__(self):
        self.x = 0
        self.y = 0
    def init_from_x_y(x,y):
        v = Vector()
        v.x = x
        v.y = y
        return v
    def add(self,v):
        result = Vector()
        result.x = self.x + v.x
        result.y = self.y + v.y
        return result

class Ball():
    def __init__(self):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.size = random.randrange(0,50)
        self.pos = Vector()
        self.pos.x = random.randrange(0,20)
        self.pos.y = random.randrange(0,20)
        self.vel = Vector()
        self.vel.x = random.randrange(0,10)
        self.vel.y = random.randrange(0,10)
        self.c = Circle(Point(self.pos.x,self.pos.y),self.size)
        self.c.setFill(color_rgb(self.R,self.G,self.B))

    def move(self):
        pos_old = self.pos
        self.pos = self.pos.add(self.vel)
        if (self.pos.x<0):
            self.pos.x = 0
            self.vel.x *= -1
        if (self.pos.y<0):
            self.pos.y = 0
            self.vel.y *= -1
        if (self.pos.x>500):
            self.vel.x *= -1
        if (self.pos.y>500):
            self.vel.y *= -1
        self.c.move(self.pos.x-pos_old.x,self.pos.y-pos_old.y)
    
    def draw(self,win):
        self.c.draw(win)

bs = []
win = GraphWin("Hello",500,500)

for i in range(10):
    bs.append(Ball())
for i in range(10):
    bs[i].draw(win)
while True:
    for i in range(10):
        bs[i].move()
    time.sleep(0.01)