import asyncio
import time

from websockets import serve


async def echo(websocket):
    async for message in websocket:
        print(message)
        # print(await websocket.recv())
        # time.sleep(1)
        # await websocket.send(message)


async def main():
    async with serve(echo, "localhost", 8001):
        await asyncio.Future()  # run forever


asyncio.run(main())
