import requests
import requests
import json

def get_request(url):
    response = requests.get(url)
    if response.status_code // 100 == 2 or response.status_code // 100 == 3:
        print('-----------------------------------------------------------------------------------------------------')
        print(f"{url} response code:{response.status_code}")


def graphql_request(url):
    graphql_query = '{"query": "{__schema {types {name}}"}"}'
    response = requests.post(url, json={'query': graphql_query})
    try:
        if response.status_code // 100 == 2 or response.status_code // 100 == 3:
            print(f"{url} status:{response.status_code} GraphQL supported!")
    except json.JSONDecodeError:
        print("GraphQL not supported.")