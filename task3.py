'''Задание 3. Подсчёт количества слов в файле
Напишите программу, которая подсчитывает количество слов
в текстовом файле text_file.txt и выводит результат на экран'''


import yaml

def amount_of_words(conf):
    amount = 0
    with open(conf['path_4'], 'r') as src:
        for line in src:
            amount += len(line.split())
    return amount

def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    res = amount_of_words(config)
    print(f'Количество слов в текстовом файле: {res}')


if __name__ == '__main__':
    main()