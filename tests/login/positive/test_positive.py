from tests.test_config import *
from lib.page_objects.login_page import LoginPage


class TestLoginPositive:

    def test_login_positive(self, driver, environment):
        login_page = LoginPage(driver=driver, environment=environment)
        login_page.open()

        test_cycles_page = login_page.login(environment.default_user_email, environment.default_user_password)

        assert test_cycles_page.loaded()
