import requests
import pprint

params = {
    'q' : 'JavaScript'
}

response = requests.get('https://api.github.com/search/repositories', params=params)

response_json = response.json()
# pprint.pprint(response_json)

print(f'Количество репозиториев с использованием js: {response_json['total_count']}')