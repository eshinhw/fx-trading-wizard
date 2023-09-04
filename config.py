import configparser
import json

config = configparser.ConfigParser()
config.read("config.ini")

API_KEY = config["CREDENTIAL"]["API"]
ACCOUNT_NUM = config["CREDENTIAL"]["ACCOUNT_NUM"]
ACCOUNT_CURRENCY = config["CREDENTIAL"]["ACCOUNT_CURRENCY"]


MAJOR = json.loads(config.get("INSTRUMENTS", "MAJOR_PAIRS"))
EUR_CROSS = json.loads(config.get("INSTRUMENTS", "EUR_CROSS"))
JPY_CROSS = json.loads(config.get("INSTRUMENTS", "JPY_CROSS"))
GBP_CROSS = json.loads(config.get("INSTRUMENTS", "GBP_CROSS"))
OTHER_CROSS = json.loads(config.get("INSTRUMENTS", "OTHER_CROSS"))


SMA = config["TRADING_SETUP"]["SMA"]
LMA = config["TRADING_SETUP"]["LMA"]
INTERVAL = config["TRADING_SETUP"]["INTERVAL"]
SL_PERCENT = config["TRADING_SETUP"]["SL_PERCENT"]
RISK_PER_TRADE = config["TRADING_SETUP"]["RISK_PER_TRADE"]
