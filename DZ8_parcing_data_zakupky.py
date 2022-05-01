import json
import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint
import pandas as pd
import json
import re as re
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient('localhost', 27017)
db = client['zakupky_data']
zakupky = db.zakupky

url = 'https://zakupki.gov.ru'

suffix = '/epz/order/extendedsearch/results.html'

params = {'morphology': 'on', 'search-filter': 'Дате+размещения', 'pageNumber': '1', 'sortDirection': ':false', 'recordsPerPage': '_50',
          'showLotsInfoHidden': 'false', 'sortBy': 'UPDATE_DATE', 'fz44': 'on', 'fz223': 'on', 'af': 'on',
          'ca': 'on', 'pc': 'on', 'pa': 'on', 'currencyIdGeneral': '-1'}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

response = requests.get(url + suffix, params=params, headers=headers)

dom = BS(response.text, 'html.parser')

#infozakupki = dom.find_all('div', {'search-registry-entrys-block'})
infozakupki = dom.find_all('div', {'search-registry-entry-block box-shadow-search-input'})

info_zakupki = []

for zakupki in infozakupki:
    zakupki_data = {}
    zakupki_name = zakupki.find('div', {'class': 'registry-entry__body-value'}).getText()
    company_name = zakupki.find('div', {'class': 'registry-entry__body-href'}).getText().strip()
    salary_zakupki = zakupki.find('div', {'class': 'price-block__value'}).getText().strip().replace(u'\xa0',' ')
    date_zakupki = zakupki.find('div', {'class': 'data-block__value'}).getText()

    zakupki_data['zakupki_name'] = zakupki_name
    zakupki_data['company_name'] = company_name
    zakupki_data['salary_zakupki'] = salary_zakupki
    zakupki_data['date_zakupki'] = date_zakupki

    try:
        zakupky.update_one({'zakupki_name': zakupki_data['zakupki_name']}, {'$set': zakupki_data}, upsert=True)
    except DuplicateKeyError as e:
        print(e)

    info_zakupki.append(zakupki_data)

pprint(info_zakupki)

#Возьмем из базы закупки больше 1000000 рублей.
sum_zakupky = zakupky.find({'salary_zakupki': {'$gt': 1000000}})

print()
