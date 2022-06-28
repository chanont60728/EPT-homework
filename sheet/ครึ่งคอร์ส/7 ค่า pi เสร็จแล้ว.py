import random
import math
  
circle_points= 0
square_points= 0
  
for i in range(10000):
  
    rand_x= random.uniform(0,10)
    rand_y= random.uniform(0,10)
  
    origin_dist= (rand_x)**2 + (rand_y)**2
  
    if origin_dist<100:
        circle_points+= 1
  
    square_points+= 1
  
    pi = 4*circle_points/square_points
  
print(pi)   


