"""Задание 3. Создание и обработка POST-запросов

Выберите API, который позволяет создавать ресурсы (например, JSONPlaceholder)

Напишите программу, которая:
    - Отправляет POST-запрос для создания нового поста
    - Выводит ID созданного поста и его содержимое

Задание 4. Обработка ошибок и работа с данными

Расширьте предыдущий код для обработки различных кодов состояния (например, 400, 404)
Добавьте вывод сообщения об ошибке в зависимости от полученного кода состояния"""

from typing import Dict, NoReturn
import requests
import uuid
import configparser
from handler_exceptions import handler


def read_config(config_file: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config


class TestAPI:
    def __init__(self, config: configparser.ConfigParser):
        self.url = config["task3"]["url"]

    def create_post(self) -> NoReturn:
        data: Dict[str, str] = {
            "userId": str(uuid.uuid4()),
            "title": "my first post",
            "body": "my content",
        }

        response = requests.post(self.url, json=data)

        status = response.status_code
        handler(response)

        if status != 201:
            raise Exception(f"Ошибка при создании записи: {response.text}")

        r = response.json()
        print(f"Запись создана:\n")
        for k, v in r.items():
            print(f"{k}: {v}")


def main() -> NoReturn:
    config = read_config("./config.cfg")
    test = TestAPI(config)
    test.create_post()


if __name__ == "__main__":
    main()
