from lib.page_objects.common.base_page_object import BasePageObject
from selenium.common.exceptions import NoSuchElementException


class HardwareSoftwarePage(BasePageObject):

    def open(self):
        path = '/tester-account/profile/hardware-software'
        self.driver.get(f'{self.environment.domain}{path}')
        self.wait_for_page_to_load()

    def loaded(self):
        """Checks if HardwareSoftwarePage is loaded

        :return: bool
        """

        try:
            self.driver.find_element_by_css_selector('#hardware-and-software-tabs')
            return True
        except NoSuchElementException:
            return False

    def update_device(self, os_name, new_os_name):
        """Updates device on devices list

        :param os_name: str
        :param new_os_name: str
        :raises Exception when device is not on the list
        """

        device = self.get_device(os_name)

        if not device:
            raise Exception("Device hasn't been found on device list")

        device.click()

        self.__select_os(new_os_name)

    def add_device(self, os_name):
        """Adds device to devices list

        :param os_name: str
        """

        self.driver.find_element_by_css_selector('.style__add-device-button-margin___3-u9x').click()

        self.__select_os(os_name)

    def remove_device(self, os_name):
        """Removes device from devices list

        :param os_name: str
        """

        device = self.get_device(os_name)
        remove_button = device.find_element_by_css_selector('form button')
        remove_button.click()

        self.wait_until_web_element_not_displayed(remove_button)

    def get_device(self, os_name):
        """Returns device from devices list. If device is not on list then returns None

        :param os_name: str
        :return: WebElement
        """

        device_list = self.driver.find_elements_by_css_selector('.success-element')

        matched_devices = list(filter(lambda x: x.text == os_name, device_list))

        if len(matched_devices) == 0:
            return None
        else:
            return matched_devices[0]

    def __select_os(self, os_name):
        """Selects device on device select

        :param os_name: str
        """

        select = self.driver.find_element_by_css_selector('.Select-control')
        select.click()

        self.wait_until_visible(locator='.Select-option')

        options = self.driver.find_elements_by_css_selector('.Select-option')
        for option in options:
            if option.text == os_name:
                option.click()
                break

        select.submit()

        self.wait_until_invisible(locator='.Select-control')
