#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача.

Разработать программу, которая будет отправлять запрос к сервису
прогноза погоды https://openweathermap.org/  с использованием
бесплатного плана (Free, требует регистрации на сайте)
и на основании полученных данных выводить следующую информацию:

    1. Максимальное давление за предстоящие 5 дней (включая текущий);

    2. День с минимальной разницей между ночной (night) и утренней (morn)
       температурой (с указанием значения в градусах Цельсия).

Выводить данные для Вашего города, указав либо долготу/широту,
либо идентификатор города из документации сайта.
"""


# https://github.com/csparpa/pyowm
# pip install pyowm

# https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html


from datetime import datetime
from json import dump

from pyowm import OWM
from pyowm.utils.config import get_config_from


ANS_FILE = "./task3a_answer_{date}.json"


if __name__ == "__main__":
    config = get_config_from("./task3a.json")
    owm = OWM(config["key"], config)

    reg = owm.city_id_registry()
    locations = reg.locations_for("Moscow", country="RU")
    mgr = owm.weather_manager()

    lat, lon = locations[0].lat, locations[0].lon
    one_call = mgr.one_call(lat, lon, exclude="minutely,hourly")

    week = one_call.forecast_daily[:5]  # current + 4 days

    pressures, temperatures = [], []
    for day in week:
        pressures.append(day.pressure["press"])
        temp = day.temperature("celsius")
        morn, night = temp.get("morn"), temp.get("night")
        temperatures.append(abs(night - morn))

    ans = {
        "pressure": [max(pressures), "Pa"],
        "temp_diff": [round(min(temperatures), 2), "C"],
    }
    today = str(datetime.now().date())  # pylint: disable=invalid-name
    with open(ANS_FILE.format(date=today), "w") as jsf:
        dump(ans, jsf, indent=4)
