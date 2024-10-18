'''Задание 2.
Напишите программу, которая создаёт несколько потоков для выполнения функции,
которая выводит целые числа от 1 до 10 с задержкой в 1 секунду'''


import time
from threading import Thread


def output_of_numbers(thread_id):
    for i in range(1, 11):
        print(f"Поток {thread_id}: {i}")
        time.sleep(1)

def supervisor():
    threads = []
    for i in range(3):
        thread = Thread(target=output_of_numbers, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def main():
    supervisor()

if __name__ == '__main__':
    main()