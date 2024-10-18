'''Задание 4.
Напишите программу, которая использует многопроцессность для вычисления
факториала целых чисел от 1 до 10. Каждый процесс должен вычислять факториал одного числа.'''


import multiprocessing


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def count_factorial(num):
    result = factorial(num)
    print(f"Процесс {num}: Факториал {num} равен {result}")

def supervisor():
    processes = []
    for i in range(1, 11):
        process = multiprocessing.Process(target=count_factorial, args=(i,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

def main():
    supervisor()

if __name__ == '__main__':
    main()