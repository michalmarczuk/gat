from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time


class BasePageObject:

    def __init__(self, driver, environment):
        self.__driver = driver
        self.__environment = environment

    @property
    def driver(self):
        return self.__driver

    @property
    def environment(self):
        return self.__environment

    def wait_for_page_to_load(self, timeout=10, interval=0.5):
        """Waits until loaded() returns true

        :param timeout: num
        :param interval: num
        :raises TimeoutException
        """

        end_time = time.time() + timeout
        while True:
            if self.loaded():
                return

            if time.time() > end_time:
                break
            else:
                time.sleep(interval)

        raise TimeoutException("Page hasn't been loaded")

    def wait_until_visible(self, locator, timeout=10, locator_type=By.CSS_SELECTOR):
        """Waits until web element with given locator become visible

        :param locator: str
        :param timeout: num
        :param locator_type: str
        :raises TimeoutException
        """

        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def wait_until_invisible(self, locator, timeout=10, locator_type=By.CSS_SELECTOR):
        """Waits until web element with given locator become invisible

        :param locator: str
        :param timeout: num
        :param locator_type: str
        :raises TimeoutException
        """

        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element((locator_type, locator)))

    def wait_until_web_element_not_displayed(self, web_element, interval=0.5, tries=20):
        """Waits until is_diplayed() from web element give false

        :param web_element: WebElement
        :param interval: num
        :param tries: 20
        :raises Exception
        """

        for i in range(tries):
            try:
                web_element.is_displayed()
                time.sleep(interval)
            except StaleElementReferenceException:
                return

        raise Exception("Web element is still displayed")
