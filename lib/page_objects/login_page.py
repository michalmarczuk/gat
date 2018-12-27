from lib.page_objects.common.base_page_object import BasePageObject
from lib.page_objects.test_cycles_page import TestCyclesPage
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePageObject):
    _error_message_locator = '.text-danger'

    def open(self):
        self.driver.get(self.environment.domain)
        self.wait_for_page_to_load()

    def loaded(self):
        """Checks if LoginPage is loaded

        :return: bool
        """

        try:
            return self.driver.find_element_by_css_selector('.auth')
        except NoSuchElementException:
            return False

    def failure_login(self, login, password):
        """Method for failure login tests

        :param login: str
        :param password: str
        :return: str with error message
        """

        self.__submit(login, password)

        self.wait_until_visible(locator=self._error_message_locator)

        return self.driver.find_element_by_css_selector(self._error_message_locator).text

    def login(self, login=None, password=None):
        """Sign in to app

        :param login: str
        :param password: str
        :return: TestCyclesPage
        """

        # If login or password not provided then use defaults
        if login is None:
            login = self.environment.default_user_email
        if password is None:
            password = self.environment.default_user_password

        self.__submit(login, password)

        test_cycles_page = TestCyclesPage(self.driver, self.environment)
        test_cycles_page.wait_for_page_to_load()

        return test_cycles_page

    def __submit(self, login, password):
        """Submits sign in form

        :param login: str
        :param password: str
        """

        self.driver.find_element_by_name('email').send_keys(login)

        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(password)
        password_input.submit()
