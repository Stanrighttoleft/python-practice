import requests
from bs4 import BeautifulSoup

url="https://www.lidiotrestaurant.com/"
html=requests.get(url)

bsp=BeautifulSoup(html.text, 'html.parser')
#print(bsp)

data_link=bsp.find('link',{"href":"https://www.lidiotrestaurant.com/public/js/jquery.mb.YTPlayer-master/jquery.mb.YTPlayer.min.css"})
#print(data_link.text)

data_div=bsp.find('div',{"id":"fb-root"})
#print(data_div)

data_c=bsp.find_all('div',{"class":"btn"})
print(data_c)

for info in data_c:
    print(info.text)