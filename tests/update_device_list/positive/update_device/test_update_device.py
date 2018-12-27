from tests.test_config import *
from lib.page_objects.login_page import LoginPage
from lib.page_objects.hardware_software_page import HardwareSoftwarePage

import lib.constants.common as const


class TestUpdateDevice:

    @pytest.mark.parametrize("os_name, new_os_name", [
        (const.WINDOWS_8_NAME, const.OSX_10_7_NAME)
    ])
    def test_update_device(self, os_name, new_os_name, driver, environment, rest_api_client, flow):
        # Prepare device list
        rest_api_client.authorize()
        flow.remove_all_devices()

        rest_api_client.put.add_hardware_and_software_desktop_devices(const.WINDOWS_VISTA_ID)
        rest_api_client.put.add_hardware_and_software_desktop_devices(const.WINDOWS_8_ID)

        # Start test
        login_page = LoginPage(driver=driver, environment=environment)
        login_page.open()
        login_page.login()

        hardware_software_page = HardwareSoftwarePage(driver=driver, environment=environment)
        hardware_software_page.open()

        hardware_software_page.update_device(os_name=os_name, new_os_name=new_os_name)

        updated_device = hardware_software_page.get_device(new_os_name)
        assert updated_device, f"Expected {new_os_name} OS on the list, but it hasn't been found"
