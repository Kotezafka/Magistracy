'''Задание 2. Обработка некорректного ввода
Расширьте предыдущую программу, чтобы она также обрабатывала ситуацию, когда пользователь вводит строку вместо числа.
Используйте несколько блоков except для обработки разных типов исключений'''


def dividing_numbers(a, b):
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        print('Деление на ноль запрещено')

def main():
    try:
        num1 = float(input())
        num2 = float(input())
    except ValueError:
        print('Некорректный ввод')
        exit()

    res = dividing_numbers(num1, num2)
    if res is None:
        exit()
    print(f"Результат деления: {res}")


if __name__ == '__main__':
    main()
