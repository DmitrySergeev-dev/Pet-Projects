import threading
import time
import requests

"""
Так почему же GIL освобождается при вводе-выводе, но не освобождается для счетных задач? Все дело в системных 
вызовах, которые выполняются за кулисами. В случае ввода-вывода низкоуровневые
системные вызовы работают за пределами среды выполнения Python.
Это позволяет освободить GIL, потому что код операционной системы не взаимодействует напрямую с объектами Python. GIL захватывается снова, только когда полученные данные переносятся в объект Python. Стало быть, на уровне ОС операции ввода-вывода выполняются конкурентно. 
"""


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(f'{response.status_code}\n')


def sync_read():
    sync_start = time.time()
    read_example()
    read_example()
    sync_end = time.time()
    print(f'Синхронное выполнение заняло: {sync_end - sync_start:.4f} с.')


def async_read():
    thread_1 = threading.Thread(target=read_example)
    thread_2 = threading.Thread(target=read_example)
    thread_start = time.time()
    thread_1.start()
    thread_2.start()
    print('Все потоки работают!')
    thread_1.join()
    thread_2.join()
    thread_end = time.time()
    print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')


if __name__ == '__main__':
    sync_read()
    async_read()
