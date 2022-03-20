from bs4 import BeautifulSoup 
import requests 

url= "https://www.vultr.com/pricing/#cloud-compute/"
page = requests.get(url)

content = BeautifulSoup(page.content, 'html.parser')
contentInfo = content.find_all('div', class_="pt__row-content")







