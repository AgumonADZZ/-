import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'http://tianqi.2345.com/today-54774.htm'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')


file = open('result.csv','w')
# products = soup.select('ul[class = "hours24-list wea-white-icon"]')
# for product in products:
#    describe = product.select('a[title = "现在 阴 9℃"]')[0].text
#print(describe)

for i in soup.find_all("a",attrs = {"class":'hours24-list-item'}):
    dis = i.select('b')[0].text
    describe = i.get('title')
    level = i.select('b')[1].text
    quanity = i.select('span')[0].text

    all_products = []
    all_products.append({
        "风向": dis,
        "描述": describe,
        "等级": level,
        "质量": quanity
    })
    file.write("风向:"+dis+" 等级:"+level+" 质量:"+quanity+" 描述:"+describe
    +'\n')

file.close()
