import math

def guassian(x,alpha,beta):
    power = (-1)*(((x-alpha)**2)/(2*(beta**2)))
    ans = (1/math.sqrt(2*math.pi*(beta**2)))*(2.7182818**(power))
    return ans

a = float(input())
b = float(input())
c = float(input())

print(guassian(a,b,c))