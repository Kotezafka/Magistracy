'''Задание 4. Копирование уникального содержимого одного файла в другой
Создайте программу, которая считывает строки из файла input.txt,
сохраняет только уникальные строки и записывает их в новый файл unique_output.txt'''


import yaml

def unique_content(conf):
    dict_unique_str = {}
    with open(conf['path_5'], 'r') as src:
        with open(conf['path_6'], 'w') as dst:
            for line in src:
                str_hash = hash(line.strip())
                if str_hash in dict_unique_str:
                    continue
                dict_unique_str[str_hash] = 1
                dst.write(line)

def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    unique_content(config)


if __name__ == '__main__':
    main()