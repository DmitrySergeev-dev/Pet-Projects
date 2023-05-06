import asyncio

from asyncio_learning.util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


asyncio.run(main(), debug=True)


"""
В отладочном режиме мы будем видеть информационные сообще-
ния, если сопрограмма работает слишком долго. Чтобы проверить
это, попробуем запустить следующий счетный код в задаче и посмо-
трим, будет ли напечатано предупреждение
"""