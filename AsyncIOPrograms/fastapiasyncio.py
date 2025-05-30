from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

@app.get("/slow")
async def slow_response():
    await asyncio.sleep(3)  # Simulate a slow async task
    return {"message": "This took 3 seconds"}

@app.get("/parallel")
async def run_parallel():
    async def task(msg, delay):
        await asyncio.sleep(delay)
        return f"{msg} done"

    results = await asyncio.gather(
        task("Task A", 2),
        task("Task B", 3),
        task("Task C", 1),
    )
    return {"results": results}
