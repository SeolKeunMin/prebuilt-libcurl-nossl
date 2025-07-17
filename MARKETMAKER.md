# Bitcoin Market Making Example

This repository includes an example script `bitcoin_market_maker.py` that demonstrates a very simple market making strategy using the [ccxt](https://github.com/ccxt/ccxt) exchange library.

## Requirements
- Python 3.7+
- The `ccxt` package (install with `pip install ccxt`).

## Environment Variables
The script reads configuration values from environment variables:

- `EXCHANGE_ID` – Identifier of the exchange (default: `binance`).
- `API_KEY` and `API_SECRET` – API credentials for the chosen exchange.
- `SYMBOL` – Trading pair to trade (default: `BTC/USDT`).
- `SPREAD` – Desired percentage spread between the buy and sell orders (default: `0.001` = 0.1%).
- `ORDER_SIZE` – Amount of BTC to place on each side (default: `0.001`).
- `LOOP_INTERVAL` – Seconds between order cycles (default: `15`).

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

The script continuously cancels any existing orders and places a limit buy and a limit sell order around the current mid price.

*This is a simplified example provided for educational purposes. Real trading requires careful handling of error conditions, balances, and exchange-specific constraints.*
