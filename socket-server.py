import asyncio
import random
import websockets


async def time(websocket, path):
    while True:
        dataToSend = "Hello here I come"
        await websocket.send(dataToSend)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
