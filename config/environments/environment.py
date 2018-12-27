import os
import json


class Environment:

    def __init__(self):
        self.__env = self.__load_json()

    @property
    def __environment_name(self):
        """Reads environment variable called TESTS_CONFIG_ENV_FILENAME

        :raises Exception: When TESTS_CONFIG_ENV_FILENAME is not provided in ENV VARs or it includes extension
        """

        config_env_filename = os.getenv('TESTS_CONFIG_ENV_FILENAME')

        if config_env_filename is None or config_env_filename == '' or '.' in config_env_filename:
            raise Exception('Environment variable "TESTS_CONFIG_ENV_FILENAME" must be set. '
                            'Filename only, without extension.')

        return config_env_filename

    def __load_json(self):
        """Reads JSON environment config file

        :return: dict environment json
        """

        environment_name = self.__environment_name
        environments_folder = os.path.dirname(os.path.abspath(__file__))

        with open(f'{environments_folder}/{environment_name}.json') as file:
            json_data = json.load(file)

        return json_data

    @property
    def domain(self):
        return self.__env["general"]["domain"]

    @property
    def default_user_email(self):
        return self.__env["general"]["default_user_email"]

    @property
    def default_user_password(self):
        return self.__env["general"]["default_user_password"]

    @property
    def rest_api_domain(self):
        return self.__env["rest_api"]["domain"]
