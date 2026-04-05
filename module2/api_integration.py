import requests

def get_external_data():
    url = "https://api.github.com"

    response = requests.get(url)

    return response.json()