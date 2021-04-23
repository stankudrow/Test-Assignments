#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача.

Написать программу, которая на основании запроса данных
с сайта http://www.cbr.ru/scripts/XML_daily.asp
определит курс японских йен к российскому рублю.
"""


# This program relies on lxml package,
# so `pip/conda install lxml` may be useful

from sys import argv
from bs4 import BeautifulSoup as BS
from requests import get as rget


def main(charcode: str):
    """Entry point."""
    # download currencies
    source = "http://www.cbr.ru/scripts/XML_daily.asp"
    charcode = charcode.upper()  # ensures str type and currency match
    data = BS(rget(source).text, "lxml")
    # seek for currency charcode
    value = None
    for tag in data.find_all("valute"):
        if tag.charcode.text == charcode:
            nominal = float(tag.nominal.text)
            value = float(tag.value.text.replace(",", "."))
            print(f"1 {charcode} = {value / nominal:.2f} RUB.")
            break
    return value


if __name__ == "__main__":
    for val in argv[1:]:
        main(val)
