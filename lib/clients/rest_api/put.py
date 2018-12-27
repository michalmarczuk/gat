import json
import requests

import lib.constants.common as const


class Put:

    def __init__(self, session, environment):
        self._session = session
        self._environment = environment

        self._headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': session}

    def add_hardware_and_software_desktop_devices(self, device_id=const.WINDOWS_8_ID):
        """PUT /hardware_and_software/desktop_devices - Adds new device to list

        :param device_id: int
        :return: dict
        """

        url = f"{self._environment.rest_api_domain}/hardware_and_software/desktop_devices"

        data = dict()
        data['tester[operating_system_ownerships_attributes[1][id]]'] = ''
        data['tester[operating_system_ownerships_attributes[1][operating_system_version_id]]'] = device_id

        response = requests.put(url, data=data, headers=self._headers).text

        return json.loads(response)

    def remove_hardware_and_software_desktop_devices(self, device_id):
        """PUT /hardware_and_software/desktop_devices - Removes device from list

        :param device_id: int
        :return: dict
        """

        url = f"{self._environment.rest_api_domain}/hardware_and_software/desktop_devices"

        data = dict()
        data['tester[operating_system_ownerships_attributes[0][id]]'] = device_id
        data['tester[operating_system_ownerships_attributes[0][_destroy]]'] = 1

        response = requests.put(url, data=data, headers=self._headers).text

        return json.loads(response)
