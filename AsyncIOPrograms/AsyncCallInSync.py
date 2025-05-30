import asyncio

async def say_hi():
    return "Hi"

# In main sync code
result = asyncio.run(say_hi())
print(result)
