'''Задание 2. Подсчёт стоимости заказа из файла
Напишите программу, которая считывает файл prices.txt, содержащий
информацию о товарах: название, количество и цену, и подсчитывает общую стоимость заказа'''

import yaml

def cost_the_order(conf):
    cost = 0
    with open(conf['path_3'], 'r') as src:
        for i, line in enumerate(src):
            if i == 0:
                continue
            cost += int(line.split(' ')[2])
    return cost

def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    res = cost_the_order(config)
    print(f'Общая стоимость заказа: {res}')


if __name__ == '__main__':
    main()