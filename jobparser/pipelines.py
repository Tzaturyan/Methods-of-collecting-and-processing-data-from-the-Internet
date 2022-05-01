# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import re as re
from pymongo.errors import DuplicateKeyError

class JobparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancy

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        if spider.name == 'hhru':
            item['min'], item['max'], item['curren'] = self.process_salary(item['salary'])
        else:
            item['min'], item['max'], item['curren'] = self.sj_process_salary(item['salary'])

        del (item['salary'])

        try:
            collection.update_one({'link': item['link']}, {'$set': item}, upsert=True)
        except DuplicateKeyError as e:
            print(e)

        return item

    @staticmethod
    def process_salary(salary):
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

        return salary_min, salary_max, salary_currency

    @staticmethod
    # для superjob.ru
    def sj_process_salary(salary):
        # работаем с вакансиями, где информация о зарплате есть
        if len(salary) > 1:
            # где оба поля указаны на superjob
            if len(salary) > 3:
                salary_min = int(salary[0].replace('\xa0', ''))
                salary_max = int(salary[4].replace('\xa0', ''))
                currency = salary[6]
            # указана только минимальная
            elif salary[0] == 'от':
                salary_and_curr = salary[2].split('\xa0')
                salary_min = int(salary_and_curr[0] + salary_and_curr[1])
                salary_max = None
                currency = salary_and_curr[2]
            # указана только максимальная
            elif salary[0] == 'до':
                salary_and_curr = salary[2].split('\xa0')
                salary_min = None
                salary_max = int(salary_and_curr[0] + salary_and_curr[1])
                currency = salary_and_curr[2]
            # указана фиксированная
            else:
                sal = int(salary[0].replace('\xa0', ''))
                salary_min, salary_max, currency = sal, sal, salary[2]
        # для вакансий, где информации о зарплате нет или указано 'Договорная' и т.д.
        else:
            salary_min, salary_max, currency = None, None, None
        return salary_min, salary_max, currency
