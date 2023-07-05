import requests
import pytest


# BASE_URL = 'https://restcountries.com/v3.1'

# url = f'{BASE_URL}/independent'
# params = {'status': False}

# response = requests.get(url, params=params)

API_KEY = 'ch253p1r01qroac5t89gch253p1r01qroac5t8a0'

BASE_URL = 'https://finnhub.io/api/v1'

url = f'{BASE_URL}/quote'
params = {'symbol': 'TSLA'}
headers = {'X-Finnhub-Token': API_KEY}

response = requests.get(url, params=params, headers=headers)
data = response.json()