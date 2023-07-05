import  requests
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


# create a test case
def test_get_quote_without_authentication():
    response = requests.get(f'{BASE_URL}/v1/quote?symbol=APPL')
    logger.info(f'Status Code : {response.status_code}')
    assert response.status_code == 401
    assert "Please use an API key." in response.json().get('error')

@pytest.mark.parametrize('symbol', ['APPL', 'GOOGL', 'TSLA', 'MSFT'])
def test_get_quote_symbol(symbol):
    url = f'{BASE_URL}/quote'
    params = {'symbol': symbol}
    headers = {'X-Finnhub-Token': API_KEY}

    # make a request
    response = requests.get(url, params=params, headers=headers)

    # create a json object
    data = response.json()
    logger.info(f'Testing URL: {url}, for symbol: {symbol}')
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2
    assert type(data.get('c')) in [float, int]
    assert type(data.get('pc')) in  [float, int]
    assert len(data.keys()) == 8
