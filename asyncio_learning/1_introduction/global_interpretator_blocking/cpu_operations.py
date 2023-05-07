import threading
import time

"""
Многопоточная версия работала почти столько же времени. На
самом деле даже чуть дольше! Это все из-за GIL и накладных рас-
ходов на создание и управление потоками. Да, потоки выполняются
конкурентно, но в каждый момент времени только одному из них
разрешено выполнять Python-код. А второй поток вынужден ждать
завершения первого, что сводит на нет весь смысл нескольких по-
токов.
"""


def print_fib(number: int) -> None:
    def fib(n: int):
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    print(f'fib{number} равно {fib(number)}')


def fibs_no_threading():
    print_fib(40)
    print_fib(41)


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib,
                                       args=(40,))
    forty_first_thread = threading.Thread(target=print_fib,
                                          args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()


if __name__ == '__main__':
    start = time.time()
    fibs_with_threads()
    end = time.time()
    print(f'Вычисление заняло {end - start} с')

    start = time.time()
    fibs_no_threading()
    end = time.time()
    print(f'Многопоточное вычисление заняло {end - start} с')
