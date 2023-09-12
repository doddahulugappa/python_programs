import asyncio
import websockets


async def handle_connection(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received message: {message}")
        await websocket.send(message)


start_server = websockets.serve(handle_connection, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
