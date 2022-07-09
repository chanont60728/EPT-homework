from Card import Card

n = int(input())
listOfCard = []
for i in range(n):
    txt = input()
    arr = txt.split()

    obj = Card(arr[0], arr[1])
    listOfCard.append(obj)

for i in range(n):
    print(listOfCard[i].getScore())
print("----------")

for i in range(n-1):
    print(listOfCard[i].sum(listOfCard[i+1]))
print("----------")


listOfCard.sort()

for l in listOfCard:
    print(l)
