import requests
import json

from .put import Put
from .get import Get

from config.environments.environment import Environment


class RestApiClient:

    def __init__(self):
        self._session = None
        self._environment = Environment()

    def authorize(self, email=None, password=None):
        """POST /sign_in

        :param email: str
        :param password: str
        :return: dict
        """

        if email is None:
            email = self._environment.default_user_email
        if password is None:
            password = self._environment.default_user_password

        url = f"{self._environment.rest_api_domain}/sign_in"
        headers = {'Content-Type': 'application/json'}

        data = {'tester': {'email': email, 'password': password, 'remember_me': True}}
        json_data = json.dumps(data, ensure_ascii=False)

        response = requests.post(url, data=json_data, headers=headers).text
        json_response = json.loads(response)

        auth_token = json_response['auth_token']
        self._session = auth_token

        return json_response

    @property
    def put(self):
        return Put(self._session, self._environment)

    @property
    def get(self):
        return Get(self._session, self._environment)
