"""Задача 1. Получение данных из публичного API

Выберите публичный API (например, JSONPlaceholder)
Напишите скрипт, который:
    - Отправляет GET-запрос к /posts
    - Извлекает и выводит заголовки и тела первых 5 постов

Задание 4. Обработка ошибок и работа с данными

Расширьте предыдущий код для обработки различных кодов состояния (например, 400, 404)
Добавьте вывод сообщения об ошибке в зависимости от полученного кода состояния"""

from typing import Dict, Any, List, NoReturn
import requests
from pprint import pprint
import configparser
from handler_exceptions import handler


def read_config(config_file: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config


class TestAPI:
    def __init__(self, config: configparser.ConfigParser):
        self.url = config["task1"]["url"]

    def get_posts(self) -> NoReturn:
        response = requests.get(self.url)

        status = response.status_code
        handler(response)

        if status != 200:
            raise Exception(f"Ошибка запроса: {response.text}")

        posts = response.json()

        arr_answers: List[Dict[str, Any]] = []
        for i, post in enumerate(posts[:5]):
            arr_answers.append(
                {"answer_id": i + 1, "title": post["title"], "body": post["body"]}
            )

        pprint(arr_answers)


def main() -> NoReturn:
    config = read_config("./config.cfg")
    test = TestAPI(config)
    test.get_posts()


if __name__ == "__main__":
    main()
