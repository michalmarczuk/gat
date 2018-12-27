class Flow:

    def __init__(self, rest_api_client):
        self._rest_api_client = rest_api_client

    def remove_all_devices(self):
        hardware_and_software = self._rest_api_client.get.hardware_and_software()
        desktop_os_list = hardware_and_software['data']['desktop_operating_systems_ownerships']
        desktop_os_ids = list(map(lambda a: a['id'], desktop_os_list))

        for desktop_os_id in desktop_os_ids:
            self._rest_api_client.put.remove_hardware_and_software_desktop_devices(desktop_os_id)
