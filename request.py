import requests

url="https://www.104.com.tw/"
html=requests.get(url)
#print(html.text)

word=html.text.splitlines()

time=0

for txt in word:
    if "104" in txt: time+=1
    
print("{} times the key word shows".format(time))
