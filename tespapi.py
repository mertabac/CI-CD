import requests

api_key = "cf645235-8d05-48c8-a201-ad6079668737"

def get_exchanges(api_key):
    url = "https://api.coinalyze.net/v1/exchanges"
    headers = {"api_key": api_key}
    response = requests.get(url, headers=headers)
    return response.json()

a = get_exchanges(api_key)

print(a)