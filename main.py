from bs4 import BeautifulSoup
import requests
import sys
import csv
import json

def scrap_vultr():
    url = "https://www.vultr.com/pricing/#cloud-compute/"
    page = requests.get(url)
    content = BeautifulSoup(page.content, "html.parser")
    contentInfo = content.find_all("div", class_="pt__row")
    info_list = []
    for block in contentInfo:
        possible_price = block.find( "div", class_="pt__cell js-price pt__cell--price pt__cell-price")
        if possible_price is None:
            break
        price = possible_price.text.replace("\xa0", "")
        machine_type = block.find_previous("h3").text.replace("\n", "").replace("\t", "")
        cpu = block.find("div", class_="pt__cell js-price").text.replace("\xa0", "")
        memory = block.find("div", class_="pt__cell js-price").find_next_sibling().text.replace("\xa0", "")
        bandwidth = block.find("div", class_="pt__cell js-price").find_next_sibling().find_next_sibling().text.replace("\xa0", "")
        storage = block.find("div", class_="pt__cell js-price").find_next_sibling().find_next_sibling().find_next_sibling().text.replace("\xa0", "")
        parsed_info = {
            "cpu": cpu,
            "memory": memory,
            "storage": storage,
            "bandwidth": bandwidth,
            "price": price,
            "machine_type": machine_type
        }
        info_list.append(parsed_info)
    return info_list

info_list = scrap_vultr()

if len(sys.argv) == 1:
    print("Fornecer argumento de saida")
else:
    if sys.argv[1] == '--save_json':
     with open('output.json', 'w', newline='') as jsonfile:
         json.dump(info_list, jsonfile)

    if sys.argv[1] == '--save_csv':
     with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = list(info_list[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for el in info_list:
            writer.writerow(el)

    if sys.argv[1] == '--print':
        print(info_list)










