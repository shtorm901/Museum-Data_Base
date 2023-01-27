import requests


def check_login(login: str, password:str):
    data = f'{{"login": "{login}", "password": "{password}" }}'
    req = requests.post('http://127.0.0.1:8000/user/login', data=data)
    answer = req.json()
    code = answer["code"]
    message = answer["message"]

    if code != 200:
        print(f"Server error:{message}")
        return None
    else:
        return answer["post"][0]
