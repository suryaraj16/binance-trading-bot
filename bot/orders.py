from bot.client import get_client
import logging

client = get_client()
logger = logging.getLogger()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Placing order: {symbol}, {side}, {order_type}, {quantity}, {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise
