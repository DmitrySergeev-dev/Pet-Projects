import asyncio

async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1

###########################
# запуск сопрограммы вне цикла событий
function_result = add_one(1)
coroutine_result = coroutine_add_one(1)
print(f'Результат функции равен {function_result}, а его тип равен {type(function_result)}')
print(f'Результат сопрограммы равен {coroutine_result}, а его тип равен {type(coroutine_result)}')

###########################
# запуск сопрограммы в цикле событий
print("А теперь запускаем сопрограмму и получаем:")
result = asyncio.run(coroutine_add_one(1))
print(result)

###########################
# Использование ключевого слова await
async def main():
    print("Использование ключевого слова await.\n"
          "Этот код работает также как и последовательный")
    one_plus_one = await coroutine_add_one(1)
    two_plus_one = await coroutine_add_one(2)
    print(one_plus_one)
    print(two_plus_one)

asyncio.run(main())
