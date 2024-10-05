'''Задание 6. Обработка ошибок импорта модулей
Напишите программу, которая импортирует модуль math и использует функцию sqrt() для вычисления
квадратного корня числа, введённого пользователем. Используйте обработку исключений для корректной
обработки ситуаций, когда модуль math не может быть импортирован или функция sqrt() не может
быть вызвана для отрицательного числа'''


class ModuleCannotImported(Exception):
    pass

class NegativeNumbers(Exception):
    pass

def calculating_square_root(n):
    try:
        import math
    except ImportError:
        raise ModuleCannotImported('Модуль math не может быть импортирован')

    try:
        square_root = math.sqrt(n)
    except:
        raise NegativeNumbers('Функция не используется для отрицательных чисел')

    return square_root

def main():
    num = float(input())
    res = calculating_square_root(num)
    print(f"Квадратный корень числа {num}: {res}")


if __name__ == '__main__':
    main()