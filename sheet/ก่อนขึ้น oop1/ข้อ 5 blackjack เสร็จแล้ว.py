def blackjack(a,b):
    if a>21 and b>21:
        return(0) 
    elif a>=b and a<=21:
        return(a)
    elif b>21:
        return(a)
    elif a>21:
        return(b)
    elif a<b and b<=21:
        return(b)
x = int(input())
y = int(input())
ans = blackjack(x,y)
print(ans)