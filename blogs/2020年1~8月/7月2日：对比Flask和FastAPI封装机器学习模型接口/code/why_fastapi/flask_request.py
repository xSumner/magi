import requests

people = [
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": "female", "Embarked": "C"},
    {"Age": 3, "Sex": "male", "Embarked": "C"},
    {"Age": 21, "Sex": "male", "Embarked": "S"}
    ]

api_url = "http://127.0.0.1:12345/predict"
my_request = requests.post(api_url, json=people).json()
print(my_request)