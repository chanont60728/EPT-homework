def power(a,b):
    return a**b

def fac(x):
    sum=1
    for i in range(1,x+1):
        sum=sum*i
    return sum

def sin(x):
    sum=0
    i=1
    while i<=17:
        if i%4==1:
            sum=sum+(power(x,i)/fac(i))
        else:
            sum=sum-(power(x,i)/fac(i))
        i=i+2
        return sum

print(sin(3.14159/2))