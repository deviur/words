#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?


Программа подсчёта количества кликов по ключевым словам в поисковой системе Яндекс.

Программа принимает csv-файл из выгрузки Яндекс.Вебмастера и выдаёт результать на экран.

Использование:
keywordstat2.py < yandex-stat-file.csv > output.csv
"""
import csv
import re
import sys

# Версия с использованием функций def
# TODO Переделать программу, чтобы использовать модули
# TODO Убрать лишние действия со словарями

VERSION = '0.2.0'


# Функция: Подсчёт общего количества кликов (clicks) по каждому запросу (query).
# Функция возвращает список словарей, в котором строка запроса является ключом.
def total_query_clicks(input_csv):
    clicks = 0
    queries = []
    query = ""

    for line in input_csv:
        for key, value in line.items():
            if key == 'Query':
                query = value
                clicks = 0
            else:
                clicks += float(value)

        queries.append(dict(Query=query, Clicks=clicks))

    return queries


# Функция: Разбивка запроса на слова и подсчёт общей суммы кликов по каждому слову.
# Функция возвращает словарь вида {word: total_clicks, ...}
def total_keyword_clicks(queries):
    keywords = {}

    for query in queries:
        words = re.findall('[a-zA-Zа-яА-ЯёЁ]+', query['Query'])

        for word in words:
            if word in keywords:
                keywords[word] += query['Clicks']
            else:
                keywords[word] = query['Clicks']

    return keywords


# Функция: Сортировка словаря по значению
# Функция возвращает упорядоченный список кортежей
def sort_dict_value(dict_, reverse=False):
    list_ = list((dict_.items()))
    list_.sort(key=lambda i: i[1])
    list_.reverse() if reverse else None
    return list_


def output_csv(list_):
    print('Word, Total')
    for key, value in list_:
        print(f"{key}, {value}")


def main():
    # Загрузить csv-файл для обработки в упорядоченный словарь
    input_csv = csv.DictReader(sys.stdin)

    # Подсчитать общее количество кликов по каждому запросу
    queries = total_query_clicks(input_csv)

    # Подсчитать общее количество кликов по каждому ключевому слову
    keywords = total_keyword_clicks(queries)

    # Сортировка словаря по значению
    keywords = sort_dict_value(keywords, reverse=True)

    # Вывод результатов
    output_csv(keywords)


if __name__ == "__main__":
    main()
