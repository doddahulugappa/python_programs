import asyncio
import websockets


async def send_message():
    async with websockets.connect("ws://localhost:8000") as websocket:
        response = await websocket.recv()
        print(f"Received response: {response}")


asyncio.get_event_loop().run_until_complete(send_message())