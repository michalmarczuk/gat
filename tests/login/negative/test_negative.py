from lib.page_objects.login_page import LoginPage
import lib.constants.common as const
from tests.test_config import *
import pytest


class TestLoginNegative:

    @pytest.mark.parametrize("login, password, expected", [
        ('test@test.pl', '', const.EMPTY_PASSWORD_MESSAGE),
        ('test@test.pl', 'pass', const.INVALID_CREDENTIALS_MESSAGE),
        ('test@testpl', 'pass', const.INVALID_EMAIL_MESSAGE)
    ])
    def test_login_negative(self, login, password, expected, driver_scope_module, environment):
        login_page = LoginPage(driver=driver_scope_module, environment=environment)
        login_page.open()

        error_message = login_page.failure_login(login, password)

        assert error_message == expected
