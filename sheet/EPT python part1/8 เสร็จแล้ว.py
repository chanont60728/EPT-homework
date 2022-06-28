import requests
import re

#link = "https://moxie.foxnews.com/feedburner/world.xml"
link = "https://www.foxnews.com"
f = requests.get(link)
text = f.text

tag = "title"
reg_str = "<" + tag + ">(.*?)</" + tag + ">"
res = re.findall(reg_str, text)

for i in res:
    print(i)