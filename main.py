import requests
import pprint

response = requests.get('http://api.github.com')

print(response.text)
response_json = response.json()
pprint.pprint(response_json)

# print(response.status_code)
# if response.ok:
#     print('Запрос успешно выполнен')
# else:
#     print('Произошла ошибка')