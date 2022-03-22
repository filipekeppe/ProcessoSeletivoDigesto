from bs4 import BeautifulSoup 
import requests 

url= "https://www.vultr.com/pricing/#cloud-compute/"
page = requests.get(url)

content = BeautifulSoup(page.content, 'html.parser')
contentInfo = content.find_all('div', class_="pt__row-content")

for list in contentInfo:
    eachInfo = list.find('div', class_="pt__cell js-price")
    price = list.find('div', class_="pt__cell js-price pt__cell--price pt__cell-price")
    allInfo = [eachInfo, price]
    print(allInfo)
    









