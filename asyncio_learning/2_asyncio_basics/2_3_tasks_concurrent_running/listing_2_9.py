import asyncio
from asyncio_learning.util import delay
from time import perf_counter

async def main():
    start = perf_counter()
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more
    print(f'Время выполнения: {perf_counter() - start:.4f}c')
asyncio.run(main())