import requests


def get_request(url):
    response = requests.get(url)
    if response.status_code // 100 == 2 or response.status_code // 100 == 3:
        print(f"{url} response code:{response.status_code}")