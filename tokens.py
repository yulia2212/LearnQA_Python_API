import requests
import time

result = 'result'
status = 'status'

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsing_response1_text = response1.json()
print(parsing_response1_text)
parsing_text = parsing_response1_text["token"]
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": parsing_text})
print(response2.text)
if response2.text != '{"status":"Job is NOT ready"}':
    print('Job is ready')
else:
    time.sleep(parsing_response1_text["seconds"] + 1)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": parsing_text})
parsing_response3_text = response3.json()
if result in parsing_response3_text and parsing_response3_text['status'] == 'Job is ready':
    print(f"Found {result}, {status} -'Job is ready': " + response3.text)
else:
    print(f"Error! Not found {result} and {status}")

