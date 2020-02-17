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
keywordstat.py < yandex-stat-file.csv
"""

import csv
import re
import sys

VERSION = '0.1.1'
# TODO Сделать версию с функциями def

# Загрузить csv-файл для обработки
input_csv = csv.DictReader(sys.stdin)


# Подсчёт общего количества кликов (clicks) по каждому запросу (query).
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

# print(queries)
# [{'Query': 'Несколько винипухов', 'Clicks': 18.0}, {'Query': 'Винипухи сильнее всех', 'Clicks': 13.0},
# {'Query': 'без винипухов никуда', 'Clicks': 10.0}, {'Query': 'долой винипухов', 'Clicks': 7.0},
# {'Query': 'сильнее винипуха', 'Clicks': 7.0}, {'Query': 'всех на винипухов', 'Clicks': 4.0}]


# Подсчёт общего количества кликов (clicks) по каждому ключевому слову (keywords).
keywords = {}
for query in queries:
    words = re.findall('[a-zA-Zа-яА-ЯёЁ]+', query['Query'])

    for word in words:
        if word in keywords:
            keywords[word] += query['Clicks']
        else:
            keywords[word] = query['Clicks']

# print(keywords)
# {'Несколько': 18.0, 'винипухов': 39.0, 'Винипухи': 13.0, 'сильнее': 20.0, 'всех': 17.0,
# 'без': 10.0, 'никуда': 10.0, 'долой': 7.0, 'винипуха': 7.0, 'на': 4.0}


# Сортировка
list_d = list((keywords.items()))
list_d.sort(key=lambda i: i[1])
list_d.reverse()


# Вывод результатов
print(list_d)
# [('винипухов', 39.0), ('сильнее', 20.0), ('Несколько', 18.0), ('всех', 17.0), ('Винипухи', 13.0),
# ('никуда', 10.0), ('без', 10.0), ('винипуха', 7.0), ('долой', 7.0), ('на', 4.0)]
