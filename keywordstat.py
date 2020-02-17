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


# Загрузить csv-файл для обработки
input_csv = csv.DictReader(sys.stdin)

# Подсчёт общего количества кликов (clicks) по каждому запросу (query).
queries = []
for line in input_csv:
    for key, value in line.items():
        if key == 'Query':
            query = value
            clicks = 0
        else:
            clicks += float(value)

    queries.append({'Query': query, 'Clicks': clicks})

# print(queries)
# Результат:
# [{'Query': 'Несколько винипухов', 'Clicks': 18.0}, {'Query': 'Винипухи сильнее всех', 'Clicks': 13.0},
# {'Query': 'без винипухов никуда', 'Clicks': 10.0}, {'Query': 'долой винипухов', 'Clicks': 7.0},
# {'Query': 'сильнее винипуха', 'Clicks': 7.0}, {'Query': 'всех на винипухов', 'Clicks': 4.0}]
# TODO Сделать сортировку. Как?

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
# Результат:
# {'Несколько': {'Clicks': 18.0, 'Query': ['Несколько винипухов']},
# 'винипухов': {'Clicks': 39.0, 'Query': ['Несколько винипухов', 'без винипухов никуда',
#                                         'долой винипухов', 'всех на винипухов']},
# 'Винипухи': {'Clicks': 13.0, 'Query': ['Винипухи сильнее всех']},
# 'сильнее': {'Clicks': 20.0, 'Query': ['Винипухи сильнее всех', 'сильнее винипуха']},
# 'всех': {'Clicks': 17.0, 'Query': ['Винипухи сильнее всех', 'всех на винипухов']},
# 'без': {'Clicks': 10.0, 'Query': ['без винипухов никуда']}, 'никуда': {'Clicks': 10.0,
#                                                                        'Query': ['без винипухов никуда']},
# 'долой': {'Clicks': 7.0, 'Query': ['долой винипухов']}, 'винипуха': {'Clicks': 7.0, 'Query': ['сильнее винипуха']},
# 'на': {'Clicks': 4.0, 'Query': ['всех на винипухов']}}
# TODO Переделать программу. Использовать def-функции. Упросить вывод результата.


# Вывод результатов
list_d = list((keywords.items()))
list_d.sort(key=lambda i: i[1])
list_d.reverse()
print(list_d)
