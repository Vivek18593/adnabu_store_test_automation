import configparser
from pathlib import Path

config = configparser.RawConfigParser()
config_path = Path("config/config.ini")
config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('auth','BASE_URL')

    @staticmethod
    def get_password():
        return config.get('auth','PASSWORD')




