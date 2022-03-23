from bs4 import BeautifulSoup 
import requests 

url= "https://www.vultr.com/pricing/#cloud-compute/"
page = requests.get(url)

content = BeautifulSoup(page.content, 'html.parser')
contentInfo = content.find_all('div', class_="pt__row")

for list in contentInfo:
    eachInfo = list.find('div', class_="pt__cell js-price").text.replace('\xa0', '')
    memory = list.find('span', class_="is-hidden-lg-up").text.replace('\xa0', '')
    price = list.find('div', class_="pt__cell js-price pt__cell--price pt__cell-price").text.replace('\xa0', '')
    allInfo = [eachInfo, memory, price]
    print(allInfo)










