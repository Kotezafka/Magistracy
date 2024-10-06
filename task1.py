'''Задание 1. Копирование содержимого одного файла в другой
Создайте программу, которая копирует содержимое файла source.txt в новый файл destination.txt'''


import yaml

def copy_file(conf):
    with open(conf['path_1'], 'r') as src:
        with open(conf['path_2'], 'w') as dst:
            for line in src:
                dst.write(line)
        
def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    copy_file(config)


if __name__ == '__main__':
    main()