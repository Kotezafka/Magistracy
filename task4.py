'''Задание 4. Обработка ошибок индексации
Напишите программу, которая принимает от пользователя индекс элемента списка
и выводит значение этого элемента. Используйте обработку исключений для корректной обработки ситуаций,
когда пользователь вводит индекс, выходящий за пределы списка'''

import random

class ListIndexOutOfRange(Exception):
    pass

def find_value_element(random_list, ind):
    try:
        value = random_list[ind]
    except IndexError as e:
        raise ListIndexOutOfRange(f'Индекс списка выходит за пределы диапазона: {e}')

    return value

def main():
    i = int(input())
    random_list = [random.randint(1, 15) for _ in range(10)]
    res = find_value_element(random_list, i)
    print(f"Значение элемента по индексу {i}: {res}")


if __name__ == '__main__':
    main()