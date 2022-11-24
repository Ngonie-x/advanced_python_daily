# Asynchronous programming
# Asynchronous programs execute in parallel wihout blocking the main process
# This makes sure that your program doesn't waste time waiting when it could be doing something else

# async declares our function as an asynchronous operation
# await tells python that this operation can be paused until some operation is completed

# Coroutines are computer components that generalize subroutines for non-preemptive multitasking, by allowing
# execution to be suspended and resumed

import asyncio

async def some_long_operation():
    return {"key": "The Emporor's wayfinder is in the imperial vault"}

async def get_stuff_async():
    results = await some_long_operation()
    return results["key"]



async def main2():
    print("Something")
    task = asyncio.create_task(foo('some text'))
    await task
    print('Finished')
    
async def foo(text):
        print(text)
        await asyncio.sleep(1)



async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
        
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    
    value = await task1
    
    print(value)
    
    await task2

asyncio.run(main())