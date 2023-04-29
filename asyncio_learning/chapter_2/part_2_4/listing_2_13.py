"""
В asyncio есть такая возможность в виде функции asyncio.wait_for.
Она принимает объект сопрограммы или задачи и тайм-аут в секундах и возвращает сопрограмму, к которой можно применить await.
Если задача не завершилась в отведенное время, то возбуждается ис-
ключение TimeoutError и задача автоматически снимается.
Для иллюстрации работы wait_for мы рассмотрим случай, когда задаче требуется две секунды, но мы даем ей только одну. Мы перехватываем исключение TimeoutError и смотрим, была ли задача снята.
"""
import asyncio
from asyncio import TimeoutError

from asyncio_learning.util import delay


async def main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except TimeoutError:
        print("Задача заняла более 5 с, скоро она закончится!")
        result = await task


asyncio.run(main())
