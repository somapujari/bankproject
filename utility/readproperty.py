import configparser

config = configparser.RawConfigParser()
config.read(r'C:\Users\Dell\PycharmProjects\bankproject\configuration\config.ini')


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
