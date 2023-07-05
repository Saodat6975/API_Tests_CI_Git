import  requests
import pytest
# from configs.config import config
from logs.logger import logger
from random import sample
from faker import Faker



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
class TestRegister:

    # class attributes
    url = f'{BASE_URL}/register'
    fake = Faker()
    
    def test_register_with_valid_credentials(self):
        # create a dictionary that contains tha data we want to send to server
        payload = {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
        response = requests.post(self.url, json=payload)
        data = response.json()
        logger.info(f'url={self.url}')
        logger.info(f'status_code={response.status_code}')
        logger.info(response.text)
        assert response.status_code == 200
        assert len(data.keys()) == 2
        assert 'id' in data.keys()
        assert 'token' in data.keys()

    

    def test_register_with_missing_password(self):

        payload =  {
                "email": self.fake.email()
            }   
        
        response = requests.post(self.url, json=payload)
        data = response.json()
        logger.info(f'url={self.url}')
        logger.info(f'status_code={response.status_code}')
        logger.info(response.text)
        assert response.status_code == 400
        assert len(data.keys()) == 1
        assert data['error'] == 'Missing password'

    def test_register_with_missing_email(self):

        payload =  {
                "password": self.fake.password()
            }   
        response = requests.post(self.url, json=payload)
        data = response.json()
        logger.info(f'url={self.url}')
        logger.info(f'status_code={response.status_code}')
        logger.info(response.text)
        assert response.status_code == 400
        assert len(data.keys()) == 1
        assert data['error'] == "Missing email or username"

    
    # @pytest.mark.parametrize("payload", "expected_error", [
    #     ({"email": fake.email()}, 'Missing password'),
    #     ({"password": fake.password()}, 'Missing email or username'),
    #     ({"email": fake.email(),"password": fake.password()}, 'Note: Only defined users succeed registration')
    # ])
    # def test_register_with_invalid_credentials(self, payload, erxpected_error):   
    #     response = requests.post(self.url, json=payload)
    #     data = response.json()
    #     logger.info(f'url={self.url}')
    #     logger.info(f'status_code={response.status_code}')
    #     logger.info(response.text)
    #     assert response.status_code == 400
    #     assert len(data.keys()) == 1
    #     assert data['error'] == erxpected_error


    