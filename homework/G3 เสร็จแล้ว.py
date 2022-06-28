ball = ["light","dark","light","dark","light","dark","light","dark","light","dark"]

for j in range(0,len(ball)):
    for i in range(0,len(ball)-1-j):
        if ball[i] != "light":
            t = ball[i]
            ball[i] = ball[i+1]
            ball[i+1] = t

print(ball)