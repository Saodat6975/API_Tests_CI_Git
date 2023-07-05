import requests
import pytest
# from configs.config import config
from logs.logger import logger

import logging

logging.basicConfig(
    filename=r'.\logs\automation.log', 
    encoding='utf-8', 
    level=logging.INFO, 
    force=True,
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p'
    )

logger = logging.getLogger()




BASE_URL = 'https://finnhub.io/api/v1'
API_KEY = 'ch253p1r01qroac5t89gch253p1r01qroac5t8a0'


# create our test data
expected_data = [
    ('AAPL', 'US', 'USD', '1980-12-12', 'Apple Inc'),
    ('TSLA', 'US', 'USD', '2010-06-09', 'Tesla Inc'),
    ('MSFT', 'US', 'USD', '1986-03-13', 'Microsoft Corp')
]
@pytest.mark.parametrize('symbol, expected_country, expected_currency, expected_ipo, expected_name,', expected_data)
def test_stock_profile(symbol, expected_country, expected_currency, expected_ipo, expected_name):
    url = f'{BASE_URL}/stock/profile2'
    params = {'symbol': symbol}
    headers = {'X-Finnhub-Token': API_KEY}

    # make a request
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    # make assertions
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    assert data['country'] == expected_country
    assert data['currency'] == expected_currency
    assert data['ipo'] == expected_ipo
    assert data['name'] == expected_name
    assert data['ticker'] == symbol
