# 1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
# записывающую собранные вакансии в созданную БД

# Импорт библиотек
from pymongo import MongoClient
import pandas as pd
from pprint import pprint
from pymongo.errors import DuplicateKeyError

# Подключение к БД
client = MongoClient('localhost', 27017)
db = client['db_vacancies']

hh = db.hh

# Загрузка датафреймов
df_hh = pd.read_csv('df_vacancies_hh_data_analytic.csv')

def mongo_DB(df, collection):
    for i in range(df.shape[0]):
        vac = df.loc[i]
        dictionary = {
            'name': vac['vacancy_name'],
            'link': vac["vacancy_link"],
            'website': vac["vacancy_website"],
            'salary_min': vac["salary_min"],
            'salary_max': vac['salary_max'],
            'currency': vac["salary_currency"]
        }

        try:
            collection.update_one({'link': dictionary['link']}, {'$set': dictionary}, upsert=True)
        except DuplicateKeyError as e:
            print(e)

mongo_DB(df_hh, hh)


# 2) Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введенной суммы

def search_by_salary(collection, limit):
    vacancies = collection.find({'$or': [{'salary_min': {'$gt': limit}}, {'salary_max': {'$gt': limit}}]})
    for vacancy in vacancies:
        pprint(vacancy)

search_by_salary(hh, 40000)

