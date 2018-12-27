import pytest

from config.environments.environment import Environment
from lib.clients.rest_api.client import RestApiClient
from lib.clients.selenium.client import SeleniumClient
from lib.utilities.flow import Flow


@pytest.fixture
def driver():
    d = SeleniumClient().driver
    yield d
    d.close()
    d.quit()


@pytest.fixture(scope='module')
def driver_scope_module():
    d = SeleniumClient().driver
    yield d
    d.close()
    d.quit()


@pytest.fixture
def rest_api_client():
    rac = RestApiClient()
    yield rac


@pytest.fixture
def environment():
    env = Environment()
    yield env


@pytest.fixture
def flow(rest_api_client):
    f = Flow(rest_api_client)
    yield f
