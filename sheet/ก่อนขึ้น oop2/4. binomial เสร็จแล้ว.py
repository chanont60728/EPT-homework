def factorial(start, end):
    res = 1
    for i in range(start, end + 1):
        res *= i  
    return res
 
def easyline(n):
    return int(factorial(n + 1, 2 * n)/factorial(1, n))
  
n = int(input("ใส่เลข n: "))
print(easyline(n))

 