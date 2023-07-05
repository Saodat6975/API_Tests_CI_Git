import requests
import pytest
from logs.logger import logger

@pytest.fixture(autouse=True)
def setup(request):
    logger.info(f'############# TEST NAME: {request.node.name} #############')

    yield #now let the test run

    # run after each test 
    logger.info(f'############# END OF THE TEST #############\n')
