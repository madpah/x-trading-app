import os
from configparser import RawConfigParser


class Config:
    class ConfigParser:
        def __init__(self):
            config_file_path = os.getenv('CONFIG_FILE')

            if not config_file_path:
                raise NoConfigFileSuppliedException

            if not os.path.exists(config_file_path):
                raise ConfigFileDoesNotExistException

            with open(config_file_path, 'r') as raw_config_file:
                self._config = RawConfigParser(allow_no_value=True)
                self._config.read_file(raw_config_file)
                raw_config_file.close()

        def get(self) -> RawConfigParser:
            return self._config

    _instance: ConfigParser = None

    def __new__(cls):
        if not Config._instance:
            Config._instance = Config.ConfigParser()

        return Config._instance


class NoConfigFileSuppliedException(Exception):
    pass


class ConfigFileDoesNotExistException(Exception):
    pass
