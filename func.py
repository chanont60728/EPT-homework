def fac(x):
    sum = 1
    for i in range(1,x+1):
        sum = sum*i
    return sum

x = fac(5)
print(x)