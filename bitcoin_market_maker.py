import os
import time
import logging

try:
    import ccxt
except ImportError:
    raise SystemExit("ccxt library is required. Install with `pip install ccxt`." )

EXCHANGE_ID = os.getenv("EXCHANGE_ID", "binance")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
SYMBOL = os.getenv("SYMBOL", "BTC/USDT")
SPREAD = float(os.getenv("SPREAD", "0.001"))  # 0.1% default spread
ORDER_SIZE = float(os.getenv("ORDER_SIZE", "0.001"))
LOOP_INTERVAL = float(os.getenv("LOOP_INTERVAL", "15"))  # seconds


def create_exchange():
    exchange_class = getattr(ccxt, EXCHANGE_ID)
    return exchange_class({
        "apiKey": API_KEY,
        "secret": API_SECRET,
        "enableRateLimit": True,
    })


def cancel_all(exchange):
    orders = exchange.fetch_open_orders(SYMBOL)
    for order in orders:
        exchange.cancel_order(order["id"], SYMBOL)


def place_orders(exchange, mid_price):
    buy_price = mid_price * (1 - SPREAD / 2)
    sell_price = mid_price * (1 + SPREAD / 2)
    exchange.create_limit_buy_order(SYMBOL, ORDER_SIZE, buy_price)
    exchange.create_limit_sell_order(SYMBOL, ORDER_SIZE, sell_price)


def run_once(exchange):
    orderbook = exchange.fetch_order_book(SYMBOL)
    bid = orderbook['bids'][0][0]
    ask = orderbook['asks'][0][0]
    mid = (bid + ask) / 2
    cancel_all(exchange)
    place_orders(exchange, mid)
    logging.info(
        "Placed buy %.8f @ %.2f and sell %.8f @ %.2f" % (
            ORDER_SIZE,
            mid * (1 - SPREAD / 2),
            ORDER_SIZE,
            mid * (1 + SPREAD / 2),
        )
    )


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    exchange = create_exchange()
    while True:
        run_once(exchange)
        time.sleep(LOOP_INTERVAL)


if __name__ == "__main__":
    main()
