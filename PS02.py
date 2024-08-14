import requests
import pprint

response = requests.get('http://api.github.com')

params = {
    'q' : 'HTML'
}

response = requests.get('https://api.github.com/search/repositories', params=params)

response_json = response.json()
#pprint.pprint(response_json)
print(f'Количество репозиториев с использованием html: {response_json['total_count']}')
print(response.status_code)
if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ошибка')