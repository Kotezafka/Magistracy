"""Задание 2. Работа с параметрами запроса

Используйте API OpenWeatherMap для получения данных о погоде

Напишите программу, которая:
    - Принимает название города от пользователя
    - Отправляет GET-запрос к API и выводит текущую температуру и описание погоды

Задание 4. Обработка ошибок и работа с данными

Расширьте предыдущий код для обработки различных кодов состояния (например, 400, 404)
Добавьте вывод сообщения об ошибке в зависимости от полученного кода состояния"""

import requests
import configparser
from typing import Dict, Any, NoReturn
from handler_exceptions import handler


def read_config(config_file: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config


class TestAPI:
    def __init__(self, config: configparser.ConfigParser):
        self.url = config["task2"]["url"]
        self.key = config["task2"]["key"]
        self.lang = config["task2"]["lang"]

    def weather_information(self, city: str) -> NoReturn:
        response = requests.get(f"{self.url}?q={city}&lang={self.lang}&key={self.key}")

        status = response.status_code
        handler(response)

        if status != 200:
            raise Exception(f"Ошибка запроса: {response.text}")

        location = response.json()["location"]
        current = response.json()["current"]

        weather: Dict[str, Any] = {
            "Страна": location["country"],
            "Город": location["name"],
            "Часовой пояс": location["tz_id"],
            "Местное время": current["last_updated"],
            "Температура, С": current["temp_c"],
            "Погодные условия": current["condition"]["text"],
            "Давление, мм.рт.ст.": int(current["pressure_mb"] * 0.750064),
            "Влажность, %": current["humidity"],
            "Облачность, %": current["cloud"],
            "Скорость ветра, м/с": round(current["wind_kph"] * 0.277778, 1),
            "Направление ветра": current["wind_dir"],
            "Количество осадков, мм": current["precip_mm"],
            "Точка росы, С": current["dewpoint_c"],
            "УФ-индекс": current["uv"],
        }
        print(f"\n\nПрогноз погоды:\n")
        for k, v in weather.items():
            print(f"{k}: {v}")


def main() -> NoReturn:
    config = read_config("./config.cfg")
    city = input(
        f"Введите название города, для которого хотите узнать прогноз погоды (на русском): "
    )
    test = TestAPI(config)
    test.weather_information(city)


if __name__ == "__main__":
    main()
