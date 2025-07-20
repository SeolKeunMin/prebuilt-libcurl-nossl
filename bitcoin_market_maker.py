import os
import time
import logging
import statistics
from collections import deque

try:
    import ccxt
except ImportError:
    raise SystemExit("ccxt library is required. Install with `pip install ccxt`." )

EXCHANGE_ID = os.getenv("EXCHANGE_ID", "binance")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
SYMBOL = os.getenv("SYMBOL", "BTC/USDT")

# base parameters
SPREAD = float(os.getenv("SPREAD", "0.001"))  # base spread (0.1%)
ORDER_SIZE = float(os.getenv("ORDER_SIZE", "0.001"))
LOOP_INTERVAL = float(os.getenv("LOOP_INTERVAL", "5"))  # seconds between checks

# update logic
PRICE_CHANGE_THRESHOLD = float(
    os.getenv("PRICE_CHANGE_THRESHOLD", "0.001")
)  # 0.1% price move triggers order update

# risk management and dynamic parameters
POSITION_LIMIT = float(os.getenv("POSITION_LIMIT", "0.01"))
TARGET_POSITION = float(os.getenv("TARGET_POSITION", "0.0"))
INVENTORY_PENALTY = float(os.getenv("INVENTORY_PENALTY", "0.1"))
VOL_WINDOW = int(os.getenv("VOL_WINDOW", "30"))  # number of mid prices to track
VOL_MULTIPLIER = float(os.getenv("VOL_MULTIPLIER", "5"))
ORDER_BOOK_DEPTH = int(os.getenv("ORDER_BOOK_DEPTH", "5"))

# track previous mid price to avoid unnecessary order churn
last_mid = None


def create_exchange():
    exchange_class = getattr(ccxt, EXCHANGE_ID)
    return exchange_class({
        "apiKey": API_KEY,
        "secret": API_SECRET,
        "enableRateLimit": True,
    })


price_history = deque(maxlen=VOL_WINDOW)


def fetch_position(exchange):
    balance = exchange.fetch_balance()
    base = SYMBOL.split("/")[0]
    return balance.get(base, {}).get("total", 0)


def compute_volatility():
    if len(price_history) < 2:
        return 0.0
    mean = statistics.mean(price_history)
    if mean == 0:
        return 0.0
    return statistics.stdev(price_history) / mean


def dynamic_spread(vol):
    return SPREAD * (1 + VOL_MULTIPLIER * vol)


def cancel_all(exchange):
    orders = exchange.fetch_open_orders(SYMBOL)
    for order in orders:
        exchange.cancel_order(order["id"], SYMBOL)


def compute_mid(orderbook):
    bids = orderbook["bids"][:ORDER_BOOK_DEPTH]
    asks = orderbook["asks"][:ORDER_BOOK_DEPTH]
    best_bid = bids[0][0]
    best_ask = asks[0][0]
    return (best_bid + best_ask) / 2


def place_orders(exchange, mid_price, spread, inventory):
    inventory_bias = INVENTORY_PENALTY * (inventory - TARGET_POSITION)
    buy_price = mid_price * (1 - spread / 2) * (1 - inventory_bias)
    sell_price = mid_price * (1 + spread / 2) * (1 + inventory_bias)
    exchange.create_limit_buy_order(SYMBOL, ORDER_SIZE, buy_price)
    exchange.create_limit_sell_order(SYMBOL, ORDER_SIZE, sell_price)


def should_update(mid):
    global last_mid
    if last_mid is None:
        last_mid = mid
        return True
    change = abs(mid - last_mid) / last_mid
    if change >= PRICE_CHANGE_THRESHOLD:
        last_mid = mid
        return True
    return False


def run_once(exchange):
    orderbook = exchange.fetch_order_book(SYMBOL)
    mid = compute_mid(orderbook)
    price_history.append(mid)
    volatility = compute_volatility()
    spread = dynamic_spread(volatility)
    inventory = fetch_position(exchange)
    if abs(inventory) > POSITION_LIMIT:
        logging.warning("Position limit reached: %.4f" % inventory)
        cancel_all(exchange)
        return

    open_orders = exchange.fetch_open_orders(SYMBOL)
    if not open_orders or should_update(mid):
        cancel_all(exchange)
        place_orders(exchange, mid, spread, inventory)
        logging.info(
            "updated orders mid %.2f spread %.4f inventory %.4f"
            % (mid, spread, inventory)
        )
    else:
        logging.info(
            "no update needed mid %.2f spread %.4f inventory %.4f"
            % (mid, spread, inventory)
        )


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    exchange = create_exchange()
    while True:
        run_once(exchange)
        time.sleep(LOOP_INTERVAL)


if __name__ == "__main__":
    main()
