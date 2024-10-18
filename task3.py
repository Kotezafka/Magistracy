'''Задание 3.
Напишите программу, которая асинхронно обрабатывает список чисел, вычисляя их квадрат.
Каждая операция обработки должна имитировать задержку в 1 секунду.'''


import asyncio


async def counts_squares():
    for i in range(1, 11):
        print(i ** 2)
        await asyncio.sleep(1)

async def main():
    task_1 = asyncio.create_task(counts_squares())
    await task_1

if __name__ == '__main__':
    asyncio.run(main())