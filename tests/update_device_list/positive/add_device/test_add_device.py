from tests.test_config import *
from lib.page_objects.login_page import LoginPage
from lib.page_objects.hardware_software_page import HardwareSoftwarePage

import lib.constants.common as const


class TestAddDevice:

    @pytest.mark.parametrize("os_name", [
        const.WINDOWS_8_NAME
    ])
    def test_add_device(self, os_name, driver, environment, rest_api_client, flow):
        # Prepare device list
        rest_api_client.authorize()
        flow.remove_all_devices()

        # Start test
        login_page = LoginPage(driver=driver, environment=environment)
        login_page.open()
        login_page.login()

        hardware_software_page = HardwareSoftwarePage(driver=driver, environment=environment)
        hardware_software_page.open()

        hardware_software_page.add_device(os_name=os_name)

        added_device = hardware_software_page.get_device(os_name)
        assert added_device, f"Expected {os_name} OS on the list, but it hasn't been found"
