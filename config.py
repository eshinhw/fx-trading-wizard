import configparser

config = configparser.ConfigParser()
config.read("config.ini")
API_KEY = config["CREDENTIAL"]["API"]
ACCOUNT_NUM = config["CREDENTIAL"]["ACCOUNT_NUM"]
