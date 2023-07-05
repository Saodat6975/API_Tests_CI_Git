import  requests
import pytest
# from configs.config import config
from logs.logger import logger
from random import sample
import json


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


BASE_URL = 'https://reqres.in/api'

# create a class
class TestUsers:

    # class attributes
    url = f'{BASE_URL}/users'


    @pytest.mark.parametrize("id", sample(range(1, 13), 6))
    def test_view_user_by_id(self, id):
        endpoint = f'{self.url}/{id}'
        response = requests.get(endpoint)
        data = response.json()

        logger.info(f'url={endpoint}')
        logger.info(f'status_code={response.status_code}')
        assert response.status_code == 200
        assert len(data.keys()) == 2
        assert 'data' in data.keys()
        assert 'support' in data.keys()
        assert data['data']['id'] == id
    

    def test_create_user_from_json_file(self):
        with open('./data/user.json') as json_file:
            payload = json.load(json_file)
        url = f'{BASE_URL}/users'
        response = requests.post(self.url, json=payload)
        data = response.json()
        logger.info(f'url={self.url}')
        logger.info(f'status_code={response.status_code}')
        logger.info(f'Payload: {payload}')
        logger.info(response.text)  
        assert response.status_code == 201
        assert len(data.keys()) == 4
        assert data['name'] == payload['name']
        assert data['job'] == payload['job']        
        assert 'id' in data.keys()
        assert 'createdAt' in data.keys()