first_str = input("")
second_str = input("")

if len(first_str)>len(second_str):
    mak_str = first_str
    noi_str = second_str
else:
    mak_str = second_str
    noi_str = first_str

count=0
for i in noi_str:
    if i in mak_str:
        count=count+1
        noi_str = noi_str.replace(i,"",1)
        mak_str = mak_str.replace(i,"",1)

print(count)