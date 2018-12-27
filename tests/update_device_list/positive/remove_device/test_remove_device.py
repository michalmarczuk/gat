from tests.test_config import *
from lib.page_objects.login_page import LoginPage
from lib.page_objects.hardware_software_page import HardwareSoftwarePage

import lib.constants.common as const


class TestRemoveDevice:

    @pytest.mark.parametrize("os_name, os_id", [
        (const.WINDOWS_8_NAME, const.WINDOWS_8_ID)
    ])
    def test_remove_device(self, os_name, os_id, driver, environment, rest_api_client, flow):
        # Prepare device list
        rest_api_client.authorize()
        flow.remove_all_devices()

        rest_api_client.put.add_hardware_and_software_desktop_devices(os_id)

        # Start test
        login_page = LoginPage(driver=driver, environment=environment)
        login_page.open()
        login_page.login()

        hardware_software_page = HardwareSoftwarePage(driver=driver, environment=environment)
        hardware_software_page.open()

        hardware_software_page.remove_device(os_name=os_name)

        removed_device = hardware_software_page.get_device(os_name)
        assert removed_device is None, f"Expected empty list, but got {os_name} on the list"
