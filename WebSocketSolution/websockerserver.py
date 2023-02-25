#!/usr/bin/env python

import asyncio
from websockets import connect


async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world! I am good1")
        await websocket.send("Hello world! I am good2")
        await websocket.send("Hello world! I am good3")
        await websocket.send("Hello world! I am good4")
        await websocket.send("Hello world! I am good5")
        print(await websocket.recv())
        print(await websocket.recv())
        print(await websocket.recv())
        print(await websocket.recv())



asyncio.run(hello("ws://localhost:8001"))
