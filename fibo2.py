def fibo1(n):
    a=0 
    b=1
    print(a,end=",")
    print(b,end=",")
    while b<n:
        a,b = b,a+b
        print(b,end=",")
    print("")
fibo1(100)