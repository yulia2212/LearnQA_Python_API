import requests

"""
1. Делает http-запрос любого типа без параметра method, в этом случае будет выводится текст ответа
 "Wrong method provided".
"""
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

"""
2. Делает http-запрос не из списка. Например, HEAD., в этом случае будет выводится пустой текст ответа.
"""
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

"""
3. Делает запрос с правильным значением method. В этом случае выводится текст ответа success.
"""
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"PUT"})
print(response.text)

"""
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с 
GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех 
типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает 
так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
"""

request_types = ["GET", "POST", "PUT", "DELETE"]

for type in request_types:
    for params in request_types:
        if request_types == "GET":
            response = requests.request(method = type, url = "https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method": params})
        else:
            response = requests.request(method = type, url = "https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": params})
            if type == params and response.text != '{"success":"!"}':
                print("Ошибка! Ожидалось success, а отображается" 
                      f" {response.text}")
            elif type != params and response.text == '{"success":"!"}':
                print("Ошибка! Ожидалось Wrong method provided, а отображается"
                  f" {response.text}")