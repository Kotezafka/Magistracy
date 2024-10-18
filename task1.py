'''Задание 1.
Напишите программу, которая создаёт 2 потока для вычисления квадратов и кубов целых чисел от 1 до 10'''


from threading import Thread


def counts_squares():
    squares = []
    for i in range(1, 11):
        squares.append(i ** 2)
    print(squares)

def counts_cubes():
    cubes = []
    for i in range(1, 11):
        cubes.append(i ** 3)
    print(cubes)

def supervisor():
    first_t = Thread(target=counts_squares, args=())
    second_t = Thread(target=counts_cubes, args=())
    first_t.start()
    second_t.start()

    first_t.join()
    second_t.join()

def main():
    supervisor()

if __name__ == '__main__':
    main()