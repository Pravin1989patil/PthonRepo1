import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password
