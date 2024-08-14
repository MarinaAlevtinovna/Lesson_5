import requests
import pprint

response = requests.get('https://jsonplaceholder.typicode.com/posts')

params = {
    'q' : 'userId'
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params='1')

response_json = response.json()
pprint.pprint(response_json)
