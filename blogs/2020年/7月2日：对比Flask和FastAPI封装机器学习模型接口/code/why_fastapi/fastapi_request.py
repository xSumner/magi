import requests

people = {"name": "阿伟", "age": 26, "address": "绍兴", "salary": 999999}

api_url = "http://127.0.0.1:8000/insert"
my_request = requests.post(api_url, json=people).json()
print(my_request)