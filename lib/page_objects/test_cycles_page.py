from lib.page_objects.common.base_page_object import BasePageObject
from selenium.common.exceptions import NoSuchElementException


class TestCyclesPage(BasePageObject):

    def open(self):
        path = '/tester-account/test-cycles'
        self.driver.get(f'{self.environment.domain}{path}')
        self.wait_for_page_to_load()

    def loaded(self):
        """Checks if TestCyclesPage is loaded

        :return: bool
        """

        try:
            return self.driver.find_element_by_css_selector('.style__header___3ScYQ').text == 'No Test Cases are available right now'
        except NoSuchElementException:
            return False
