import random
import time

x = []

random.seed()


for i in range(0,5000): # สุ่มมา 5000 จำนวน
    x.append(random.randrange(10000)) # สุ่มเลข 0 ถึง 10000

start = time.time()

x.sort()

end = time.time()

use_t1 = end-start
print(use_t1)