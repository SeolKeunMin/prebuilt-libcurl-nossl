# Bitcoin Market Making Example

This repository includes an example script `bitcoin_market_maker.py` that demonstrates a basic market making strategy using the [ccxt](https://github.com/ccxt/ccxt) exchange library.  
The script now includes inventory and risk management as well as a simple form of dynamic spread adjustment based on recent volatility.

## Requirements
- Python 3.7+
- The `ccxt` package (install with `pip install ccxt`).

## Environment Variables
The script reads configuration values from environment variables:

- `EXCHANGE_ID` – Identifier of the exchange (default: `binance`).
- `API_KEY` and `API_SECRET` – API credentials for the chosen exchange.
- `SYMBOL` – Trading pair to trade (default: `BTC/USDT`).
- `SPREAD` – Base percentage spread between the buy and sell orders (default: `0.001` = 0.1%).
- `ORDER_SIZE` – Amount of BTC to place on each side (default: `0.001`).
- `LOOP_INTERVAL` – Seconds between each check for order updates (default: `5`).
- `PRICE_CHANGE_THRESHOLD` – Fractional price move that triggers new orders (default: `0.001`).
- `POSITION_LIMIT` – Maximum absolute BTC position before trading stops (default: `0.01`).
- `TARGET_POSITION` – Desired neutral inventory level (default: `0`).
- `INVENTORY_PENALTY` – Price adjustment factor per BTC of inventory difference (default: `0.1`).
- `VOL_WINDOW` – Number of mid prices to use when computing volatility (default: `30`).
- `VOL_MULTIPLIER` – Multiplier used in dynamic spread calculation (default: `5`).
- `ORDER_BOOK_DEPTH` – Number of levels from the order book used for the mid price (default: `5`).

## Usage
1. Install the required package:

   ```bash
   pip install ccxt
   ```

2. Export your API credentials and other parameters, then run the script:

   ```bash
   export API_KEY=YOUR_KEY
   export API_SECRET=YOUR_SECRET
   python bitcoin_market_maker.py
   ```

The script checks the market every few seconds and only cancels and replaces orders when the mid price has moved more than `PRICE_CHANGE_THRESHOLD`.

*This is a simplified example provided for educational purposes. Real trading requires careful handling of error conditions, balances, and exchange-specific constraints.*
