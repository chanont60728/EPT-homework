def power2(a,n):
    if n==0:
        return 1
    return a*power2(a,n-1)

print(power2(2,100))