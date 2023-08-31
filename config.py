import configparser

config = configparser.ConfigParser()
config.read("config.ini")
API_KEY = config["CREDENTIAL"]["API"]
TF_ACCOUNT = config["TREND_FOLLOWING"]["TF_ACCOUNT"]
