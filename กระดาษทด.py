class Foo(object):

     def __init__(self, score):
         self.score = score

     def __lt__(self, other):
         return self.score < other.score

l = [Foo(3), Foo(1), Foo(2),Foo(100),Foo(20),Foo(0)]
l.sort()

for r in l:
    print(r.score)

print("3"<"10")