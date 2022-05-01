import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint
import re as re
import pandas as pd
import json
from pymongo import MongoClient
import pymongo as pymongo

client = MongoClient('localhost', 27017)
db = client['vacan_data']
vacancy_hh = db.vacancy_hh
#vacancy_hh.deleteMany({})
#vacancy_hh.create_index([('vacancy_link', pymongo.TEXT)], name='search_index', unique=True)

url = 'https://hh.ru'

suffix = '/search/vacancy/'

params = {'area': '1', 'fromSearchLine': 'true', 'text': 'Data Science', 'page': ':3', 'per_page': '60',
          'clusters': 'true', 'no_magic': 'true', 'ored_clusters': 'true', 'enable_snippets': 'true', 'from': 'suggest_post',
          'only_with_salary': 'true', 'showClusters': 'true'}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

response = requests.get(url + suffix, params=params, headers=headers)

dom = BS(response.text, 'html.parser')

infovacan = dom.find_all('div', {'vacancy-serp-item-body__main-info'})



info_vacancy = []

for vacancy in infovacan:
    vacancy_data = {}
    vacancy_name = (vacancy.find('span', {'class': 'g-user-content'})).findChild().getText()
    vacancy_link = vacancy.find('span', {'class': 'g-user-content'}).findChild().get('href')
    vacancy_website = url
    salary = vacancy.find('span', {'bloko-header-section-3'}).text.replace(u'\u202f', u'')
    if not salary:
        salary_min = None
        salary_max = None
        salary_currency = None
    else:
        salary_currency = (re.sub(r"\d", '', salary)).split()[-1]
        try:
            salaries = salary.split()
            salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
            salary_min = float(salaries[0])
        except:
            salaries = salary.split('-')
            salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
            salary_min = float(salaries[0])
        if len(salaries) > 1:
            try:
                salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
                salary_max = float(salaries[1])
            except:
                salaries[2] = re.sub(r'[^0-9]', '', salaries[2])
                salary_max = float(salaries[2])
        else:
            salary_max = None
    vacancy_data['vacancy_name'] = vacancy_name
    vacancy_data['vacancy_link'] = vacancy_link
    vacancy_data['vacancy_website'] = vacancy_website
    vacancy_data['salary_min'] = salary_min
    vacancy_data['salary_max'] = salary_max
    vacancy_data['salary_currency'] = salary_currency

    info_vacancy.append(vacancy_data)

    try:
        vacancy_hh.update_one({'vacancy_link': vacancy_data['vacancy_link']}, {'$set': vacancy_data}, upsert=True)
    except DuplicateKeyError as e:
        print(e)

pprint(info_vacancy)

#print(pd.DataFrame(info_vacancy))

#with open('hh_parcing.json', 'w') as hh:
    #json.dump(info_vacancy, hh)


print()