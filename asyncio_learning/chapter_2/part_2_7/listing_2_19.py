import asyncio

from asyncio_learning.util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))
    await task_one
    await task_two
    await delay_task


asyncio.run(main())

"""
Кажется, что эта программа должна работать столько же, сколько
программа в листинге 2.18. Разве delay_task не будет выполняться
конкурентно со счетными задачами? Нет, не будет, потому что мы
сначала создали две счетные задачи и тем самым не даем циклу со-
бытий выполнить что-то еще. Следовательно, время работы прило-
жения будет равно сумме времен работы задач cpu_bound_work плюс
4 с, которые займет задача delay.
Если требуется выполнить счетную работу и все-таки использовать
async / await, то это можно сделать. Но придется воспользоваться
многопроцессностью и попросить asyncio выполнять наши задачи
в пуле процессов. 
"""
