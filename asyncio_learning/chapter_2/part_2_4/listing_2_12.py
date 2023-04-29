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
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except TimeoutError:
        print("Тайм-аут!")
        print(f'Задача была снята? {delay_task.cancelled()}')


asyncio.run(main())
