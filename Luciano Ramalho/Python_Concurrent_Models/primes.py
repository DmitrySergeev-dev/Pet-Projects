import asyncio
import math
import random


def is_prime(n: int) -> bool:
    """Счетная функция для проверки числа на простоту
    Вызовите ее в функции supervisor для проверки
    влияния GIL на работу конкурентных программ"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


NUMBERS = [random.randint(2 ^ 53, 9_999_999_999_999_999) for i in range(20)]



async def async_is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
        if i % 100_000 == 1:
            await asyncio.sleep(0)
    return True


if __name__ == '__main__':
    is_prime(5_000_111_000_222_021)
    # print(NUMBERS, len(NUMBERS))
