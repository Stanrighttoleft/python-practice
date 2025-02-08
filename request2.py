import requests
from bs4 import BeautifulSoup

url="https://www.tripadvisor.com/Restaurants-g297910-oa90-Taichung.html"
html=requests.get(url)

bsp=BeautifulSoup(html.text,'html.parser')
#print(bsp)

datatitle=bsp.select("title")
print(datatitle)