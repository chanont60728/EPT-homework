def isAnagram(word1,word2):
    if word1 == word2:
        return False

    word1 = list(word1)
    word2 = list(word2)

    for i in word1:
        if i in word2:
            word2.remove(i)
    
    if not word2:
        return True
    else:
        return False

word1 = input("ใส่คำเข้า word1: ")
word2 = input("ใส่คำเข้า word2: ")
print(isAnagram(word1,word2))