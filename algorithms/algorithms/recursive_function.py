def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == '__main__':
    print(countdown(10))
    print(factorial(5))

