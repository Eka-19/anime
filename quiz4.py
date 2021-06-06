import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

payload = {'start': 1}
h = {'Accept-Language': 'en-US'}
url = 'https://www.imdb.com/list/ls026392856/?st_dt=&mode=detail'

file = open('anime.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Year'])



while payload['start'] < 400:
    r = requests.get(url, params=payload, headers=h)
    print(r.url)

    # print(r)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')
    block = soup.find('div', class_='lister-list')
    all_anime = block.find_all('div', class_='lister-item')
    for each in all_anime:
        title = each.h3.a.text
        year = each.find('span', class_='lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        print(year)
        file_obj.writerow([title, year])

    payload['start'] += 100
    sleep(randint(5, 7))

