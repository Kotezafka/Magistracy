'''Задание 1. Обработка деления на ноль
Напишите программу, которая принимает два числа от пользователя и выводит результат их деления.
Используйте обработку исключений, чтобы корректно обработать ситуацию, когда пользователь
вводит 0 в качестве второго числа'''


def dividing_numbers(a, b):
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        print('Деление на ноль запрещено')
        
def main():
    num1 = float(input())
    num2 = float(input())
    res = dividing_numbers(num1, num2)
    if res is None:
        exit()
    print(f"Результат деления: {res}")


if __name__ == '__main__':
    main()
