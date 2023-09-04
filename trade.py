import os

import numpy as np

from config import ACCOUNT_NUM, ACCOUNT_CURRENCY, API_KEY
from config import SMA, LMA, INTERVAL, SL_PERCENT, RISK_PER_TRADE
from config import MAJOR, EUR_CROSS, JPY_CROSS, GBP_CROSS, OTHER_CROSS
from oanda import Oanda

# Login

if os.name == "nt":
    oanda = Oanda(API_OANDA, CROSSOVER_ACCT)
if os.name == "posix":
    oanda = Oanda(API_KEY, ACCOUNT_NUM, ACCOUNT_CURRENCY)

OPEN_ORDERS = oanda.get_order_list()
OPEN_TRADES = oanda.get_trade_list()

SYMBOLS_ORDERS = oanda.symbols_in_orders()
SYMBOLS_TRADES = oanda.symbols_in_trades()


def check_crossover(symbol):
    prices = oanda.get_prices(symbol, 365, INTERVAL)
    sma = f"{SMA}MA"
    lma = f"{LMA}MA"
    prices[sma] = prices["Close"].rolling(int(SMA)).mean()
    prices[lma] = prices["Close"].rolling(int(LMA)).mean()
    prices["50MA_lagged"] = prices[sma].shift(5)
    prices.dropna(inplace=True)

    def find_crossover(fast_sma, lagged_fast_sma, slow_sma):
        if fast_sma > slow_sma and lagged_fast_sma < slow_sma:
            return "bullish"
        if fast_sma < slow_sma and lagged_fast_sma > slow_sma:
            return "bearish"
        return "neutral"

    prices["crossover"] = np.vectorize(find_crossover)(prices[sma], prices["50MA_lagged"], prices[lma])

    print(prices)

    return prices["crossover"].iloc[-1]


def entry(symbol):
    print(f"Testing MA Crossover for {symbol}")
    try:
        # bullish cross over --> long
        if check_crossover(symbol) == "bullish":
            # Determine entry and stop price
            entry = oanda.get_current_ask_bid_price(symbol)[0]
            stop = entry - (entry * SL_PERCENT)

            if (symbol not in SYMBOLS_TRADES) and (symbol not in SYMBOLS_ORDERS):
                oanda.create_limit_order(symbol, entry, stop, RISK_PER_TRADE)
                print(f"Long Order Placed [{symbol}] @ ENTRY: {entry} SL: {stop}")
            else:
                # there exists a trade in opposite direction which must be closed first.
                oanda.close_open_trade(symbol)
                oanda.create_limit_order(symbol, entry, stop, RISK_PER_TRADE)

        # bearish cross over --> short
        elif check_crossover(symbol) == "bearish":
            # Determine entry and stop price
            entry = oanda.get_current_ask_bid_price(symbol)[1]
            stop = entry + (entry * SL_PERCENT)

            if (symbol not in SYMBOLS_TRADES) and (symbol not in SYMBOLS_ORDERS):
                oanda.create_limit_order(symbol, entry, stop, RISK_PER_TRADE)
                print(f"Short Order Placed [{symbol}] @ ENTRY: {entry} SL: {stop}")
            else:
                # there exists a trade in opposite direction which must be closed first.
                oanda.close_open_trade(symbol)
                oanda.create_limit_order(symbol, entry, stop, RISK_PER_TRADE)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    instruments = MAJOR + EUR_CROSS + JPY_CROSS + GBP_CROSS + OTHER_CROSS
    print(instruments)
    # check_crossover("EUR_USD")
    # print(INSTRUMENTS)
    # print(oanda.calculate_unit_size("EUR_USD", 1.06319, 1.05010, 0.02))
    # print(oanda.calculate_unit_size("AUD_CAD", 0.8634, 0.85118, 0.02))
    # print(oanda.calculate_unit_size("EUR_NZD", 1.81088, 1.77822, 0.02))
    # print(oanda.calculate_unit_size("GBP_AUD", 1.94612, 1.90252, 0.02))
    # print(oanda.calculate_unit_size("CAD_CHF", 0.66069, 0.67701, 0.02))
    # print(oanda.calculate_unit_size("CAD_JPY", 106.53, 105.02, 0.02))
    # print(oanda.cal_position_size("EURUSD", RISK_PER_TRADE, 1.06))

    entry(instruments[0])
