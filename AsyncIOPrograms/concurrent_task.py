import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = asyncio.create_task(say_after(1, "One"))
    task2 = asyncio.create_task(say_after(2, "Two"))

    await task1
    await task2

asyncio.run(main())
