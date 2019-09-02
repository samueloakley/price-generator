import numpy as np
import websockets
import asyncio
import datetime

async def send_prices(websocket, path):
    current_time = datetime.datetime.now()
    price = get_next_price(previous_price, current_time - previous_time) + DRIFT
    print(price)
    await websocket.send(price)

def get_next_price(p, delta_t):
    return p + delta_t**2 * np.random.normal(0, 1)

START_PRICE = 0
previous_price = START_PRICE
previous_time = datetime.datetime.now()
DRIFT = 0

start_server = websockets.serve(send_prices, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()