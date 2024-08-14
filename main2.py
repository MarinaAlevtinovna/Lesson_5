import requests

img = 'https://ir.ozone.ru/s3/multimedia-u/wc1000/6796009074.jpg'

response = requests.get(img)

with open('test.jpg', 'wb') as file:
    file.write(response.content)