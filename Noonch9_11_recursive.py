memo = {}

def c(n,k):
    if n in memo:
        return memo[n]
    if n<=2:
        k = 1
    else:
        k = c(n-1)+c(n-2)
    memo[n] = k
    return k

n = int(input())
k = int(input())
print(c(n,k))