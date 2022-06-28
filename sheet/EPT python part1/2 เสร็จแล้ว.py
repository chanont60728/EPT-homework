import math
n = int(input())

sum = 0
for i in range(1,n+1):
    sum = sum+n**i

print(math.sqrt(sum))
