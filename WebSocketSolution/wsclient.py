import asyncio
import websockets


async def send_message(message):
    async with websockets.connect("ws://localhost:8000") as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received response: {response}")


asyncio.get_event_loop().run_until_complete(send_message("Hello, world!"))