import requests
req = requests.get('https://playground.learnqa.ru/api/get_text')
print(req.text)