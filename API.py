#Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного
# пользователя, сохранить JSON-вывод в файле *.json.
import json
import requests
from pprint import pprint
url = 'https://api.github.com'
user = 'Tzaturyan'
types = 'owner'
params = {'types': types}
responce = requests.get(f'{url}/users/{user}/repos', params=params)
j_data = responce.json()
with open('data.json', 'w') as datagit:
    json.dump(j_data, datagit)
for i in responce.json():
        print(i['full_name'])

#API вконтакте (https://vk.com/dev/first_guide).
# Сделайте запрос, чтобы получить список всех сообществ на которые вы подписаны.
url2 = 'https://api.vk.com'
method = 'groups.get'
user_id = '200711998'
access_token = '9eec22f7ec951f752fd23b081cfe4a60de51e344ca1b048f0f88674b8ea7a0218c0396c110e665a0a514e'
v = 5.81
extended = 1
params = {'access_token': access_token, 'v': v, 'extended': extended}
responce2 = requests.get(f'{url2}/method/{method}', params=params)
print(responce2.text)
data = json.loads(responce2.text)
print(f"Наименования сообществ - {data.get('name')}")

with open('data2.json', 'w') as datagit:
    json.dump(data, datagit)