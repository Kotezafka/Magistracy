'''Задание 3. Создание собственных исключений
Напишите программу, которая вычисляет сумму списка целых чисел. Создайте свои собственные классы исключений
для обработки ситуаций, когда в списке есть хотя бы одно чётное или отрицательное число.
Используйте оператор raise для генерации исключений'''

import random

class EvenNumber(Exception):
    pass

class NegativeNumber(Exception):
    pass

def sum_numbers(random_list):
    sum_list = 0
    for num in random_list:
        if num % 2 == 0:
            raise EvenNumber('В списке есть чётное число')

        if num < 0:
            raise NegativeNumber('В списке есть отрицательное число')

        sum_list += num
    return sum_list

def main():
    random_list = [random.randint(-10, 10) for _ in range(10)]
    res = sum_numbers(random_list)
    print(f"Сумма списка целых чисел равна: {res}")


if __name__ == '__main__':
    main()