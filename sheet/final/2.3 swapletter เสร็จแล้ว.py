def swapletter(phrase:str,from_letter:str,to_letter:str):
    return phrase.replace(from_letter,to_letter)

phrase = input("ใส่คำ (phrase): ")
from_letter = input("ใส่ตัวอักษรตัวเดียวเท่านั้น: ")
to_letter = input("ใส่ตัวอักษรตัวเดียวเท่านั้น: ")

print(swapletter(phrase,from_letter,to_letter))
