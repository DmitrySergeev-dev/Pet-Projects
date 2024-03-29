from primes import is_prime, NUMBERS
from typing import NamedTuple
from time import perf_counter

"""sequential.py: эталон для сравнения последовательного,
многопроцессного и многопоточного выполнения счетной задачи"""


class Result(NamedTuple):
    prime: bool
    elapsed: float


def check(n: int) -> Result:
    t0 = perf_counter()
    prime = is_prime(n)
    return Result(prime, perf_counter() - t0)


def main() -> None:
    print(f'Checking {len(NUMBERS)} numbers sequentially:')
    t0 = perf_counter()
    for n in NUMBERS:
        prime, elapsed = check(n)
        label = 'P' if prime else ''
        print(f'{n:16} {label} {elapsed:9.6f}s')
    elapsed = perf_counter() - t0
    print(f'Total time: {elapsed:.2f}s')


if __name__ == '__main__':
    main()
