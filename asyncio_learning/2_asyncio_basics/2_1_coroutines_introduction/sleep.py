import asyncio


async def hello_world_message():
    await asyncio.sleep(1)  # приотсановить hello_world_message на 1 с
    return 'Hello, world!'


async def main():
    message = await hello_world_message()
    print(message)


asyncio.run(main())
