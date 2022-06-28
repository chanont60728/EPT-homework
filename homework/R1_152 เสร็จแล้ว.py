score = []
name = []
surname = []
i = 0

while i < 10:
    name.append(input("Please input name: "))
    surname.append(input("Please input surname: "))
    score.append(int(input("Please input score: ")))
    i = i+1
max_index=0
max = score[0]
i = 0
while i<len(score):
    if max < score[i]:
        max = score[i]
        max_index = i
    i = i+1
print(name[max_index]+" "+surname[max_index])