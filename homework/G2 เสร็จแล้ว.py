def pow(a,n):
    result = 1
    while n > 0:
        if n%2==1:
            result=result*a
            n=n-1
        n = n//2
        a = a*a
    return result

print(pow(2,100))