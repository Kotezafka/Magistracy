'''Задание 5. Обработка ошибок преобразования типов
Напишите программу, которая принимает от пользователя строку и преобразует её в число с плавающей точкой.
Используйте обработку исключений для корректной обработки ситуаций, когда пользователь вводит строку,
которую невозможно преобразовать в число'''

class ImpossibleConverted(Exception):
    pass

def converting_string(s):
    try:
        num = float(s)
    except:
        raise ImpossibleConverted('Строку невозможно преобразовать в число')

    return num

def main():
    s = input()
    res = converting_string(s)
    print(f"Число с плавающей точкой: {res}")


if __name__ == '__main__':
    main()