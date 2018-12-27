from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os


class SeleniumClient:
    __driver = None

    def __init__(self):
        self.__driver = self.__driver()

    def __driver(self):
        """Reads environment variable called DRIVER

        :return: WebDriver
        :raises Exception: When DRIVER is not provided in ENV VARs
        """

        driver_type = os.getenv('DRIVER')

        if driver_type is None:
            raise Exception('Driver type not set. Please add environment variable: DRIVER. '
                            'Supported types are: chrome, chrome-headless')

        if driver_type == 'chrome':
            return Chrome(options=self.__options(headless=False))
        elif driver_type == 'chrome-headless':
            return Chrome(options=self.__options(headless=True))
        else:
            raise Exception('Not supported driver type. Supported types are: chrome, chrome-headless')

    def __options(self, headless=False):
        """Prepares options for chrome driver

        :param headless: bool
        :return: Options
        :raises Exception: When DRIVER is not provided in ENV VARs
        """

        options = Options()
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

        if headless:
            options.add_argument('--headless')

        return options

    @property
    def driver(self):
        return self.__driver
