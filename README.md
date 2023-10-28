<div align="center">

  ![logo](https://github.com/eshinhw/fx-trading-wizard/assets/41933169/7dae24ae-8484-493f-a7fa-da985b73901b)

</div>

<div align="center">

  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/eshinhw/fx-trading-wizard)
  ![GitHub issues](https://img.shields.io/github/issues/eshinhw/fx-trading-wizard)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/eshinhw/fx-trading-wizard)
  
</div>

## Objectives

- Trade FX markets systematically without human emotions by following pre-determined set of rules.
- Develop, backtest and deploy a profitable trading strategy in a live market environment.

## Tech Stack

- Python: backend implementation and strategy development
- Dash: frontend dashboard

## Third Party APIs

- [OANDA API]()

## Trading Logic

### Rate Of Change (ROC)

ROC can be used to determine the overal market trend. 

- 1M / 3M / 6M / 12M ROCs can be computed and if all four ROCs are negative, we claim the market is downtrend.
- 1M / 3M / 6M / 12M ROCs can be computed and if all four ROCs are positive, we claim the market is uptrend.

For all other cases, we conclude that the market is in a range market without clear direction, and we simply don't trade those markets.

### Moving Averages Crossover

If the market has clear trend, we can use moving averages as our entry and risk management tools.

### Tradable Pairs

- Major FX pairs: EURUSD, GBPUSD, USDJPY, USDCHF, AUDUSD, NZDUSD


### Long Position

- Positive momemtum
- 50SMA above 200SMA
- Entry: 55 days high breakout
- Stop: 2 * ATR or breakout of 20 days low

### Short Position

- Negative momentum
- 50SMA below 200SMA
- Entry: 55 days low breakout
- Stop: 2 * ATR or breakout of 20 days high
