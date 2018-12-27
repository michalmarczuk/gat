import json
import requests

import lib.constants.common as const


class Get:

    def __init__(self, session, environment):
        self._session = session
        self._environment = environment

        self._headers = {'Content-Type': 'application/json', 'Authorization': session}

    def hardware_and_software(self):
        """GET /hardware_and_software

        :return: dict
        """

        url = f"{self._environment.rest_api_domain}/hardware_and_software"
        response = requests.put(url, headers=self._headers).text

        return json.loads(response)
