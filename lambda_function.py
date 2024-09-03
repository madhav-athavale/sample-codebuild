import requests
import json


def lambda_handler(event, context):
    latitude = '40.71427'
    longitude = '-74.00597'
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat=40.71427&lon=-74.00597&appid=b5cd2f38a8c37fc39dfc85ce74c1af5c"
    response = requests.get(api_url)
    json_object = json.loads(response.text)
    print("Hello")
    print(json_object)
    return json_object


if __name__ == '__main--':
    lambda_handler('', '')
