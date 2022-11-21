# Asynchronous programming
# Asynchronous programs execute in parallel wihout blocking the main process
# This makes sure that your program doesn't waste time waiting when it could be doing something else

# async declares our function as an asynchronous operation
# await tells python that this operation can be paused until some operation is completed

import asyncio

async def some_long_operation():
    return {"key": "The Emporor's wayfinder is in the imperial vault"}

async def get_stuff_async():
    results = await some_long_operation()
    return results["key"]


if __name__ == "__main__":
    results = asyncio.run(get_stuff_async())
    print(results)