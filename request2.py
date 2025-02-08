import requests
from bs4 import BeautifulSoup

url="https://www.tripadvisor.com/Restaurants-g297910-oa90-Taichung.html"
html=requests.get(url)

bsp=BeautifulSoup(html.text,'html.parser')
#print(bsp)

datatitle=bsp.select("title")
print(datatitle)

dataid=bsp.select("#cmsg")
print(dataid)

datainfo=bsp.select("html head meta")
print(datainfo)

datameta=bsp.find('meta')
print(datameta)

datametaall=bsp.find_all('meta')
print(datametaall)

datalink=bsp.find('a')
print(datalink)

datalinka=bsp.find_all('a')
print(datalinka)

datafooter=bsp.select("#footer")
print(datafooter)

#tag can use find, select is used for id