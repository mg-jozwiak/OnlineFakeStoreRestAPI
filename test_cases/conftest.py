import pytest
from routes.routes import Routes
from utils.config_reader import ReadConfig

@pytest.fixture(scope="class")
def setup():
    base_url = Routes.BASE_URL
    config_reader = ReadConfig()
    