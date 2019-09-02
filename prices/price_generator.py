import numpy as np
import websockets
import asyncio
from datetime import datetime, timedelta

START_PRICE = 0
previous_price = START_PRICE
previous_time = datetime.now()
DRIFT = 0

async def send_prices(websocket, path):
    global previous_price, previous_time
    current_time = datetime.now()
    delta_t = (current_time - previous_time).total_seconds()
    previous_time = current_time
    price = get_next_price(previous_price, delta_t) + DRIFT
    previous_price = price
    print(price)
    await websocket.send(str(price))

def get_next_price(p, delta_t):
    return p + delta_t**2 * np.random.normal(0, 1)

start_server = websockets.serve(send_prices, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()