import asyncio
import json
import time
import random

import websockets

counter = 1000
# async def main():
#     global counter
#     async with websockets.connect("ws://localhost:8000/sendVote") as websocket:
#         while counter < 100:
#             counter += 1
#             try:
#                 # a = readValues() #read values from a function
#                 # insertdata(a) #function to write values to mysql
#                 await websocket.send("some token to recognize that it's the db socket")
#                 time.sleep(3) #wait and then do it again
#             except Exception as e:
#                  print(e)
#

# asyncio.get_event_loop().run_until_complete(main())


async def callmain():
    async with websockets.connect('ws://localhost:8000/sendVote') as ws:
        while True:
            k1 = random.choice(['pizza', 'burger'])
            # k2 = random.randint(0, 1)
            await ws.send(k1)
            # time.sleep(1)
        # print(await ws.recv())



asyncio.run(callmain())


