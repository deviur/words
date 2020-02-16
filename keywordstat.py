#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Это консольное приложение для подсчёта частотности слов в запросах, по которым пришли насайт

Использование:
keywordstat.py < yandex-stat-file.csv
"""

import csv
import sys

input_csv = csv.DictReader(sys.stdin)
all_words = {}

# # for DEBUG
# if input_csv == '':
#     input_csv = """"
# Query, 2020-02-10
# Несколько винипухов, 10
# Винипухи сильнее всех, 8
# без винипухов никуда, 7
# долой винипухов, 6
# сильнее винипуха, 5
# всех на винипухов, 3
# """

# Подсчёт количества кликов (clicks) на сайт по каждому запросу (query).
num = 1
queries = []
for line in input_csv:
    for key, value in line.items():
        if key == 'Query':
            query = value
            clicks = 0
        else:
            clicks += float(value)

    queries.append({'Query': query, 'Clicks': clicks})
    num += 1

print(queries)
# [{'Query': 'Несколько винипухов', 'Clicks': 18.0}, {'Query': 'Винипухи сильнее всех', 'Clicks': 13.0},
# {'Query': 'без винипухов никуда', 'Clicks': 10.0}, {'Query': 'долой винипухов', 'Clicks': 7.0},
# {'Query': 'сильнее винипуха', 'Clicks': 7.0}, {'Query': 'всех на винипухов', 'Clicks': 4.0}]

# TODO Сделать сортировку. Как?

# Подсчёт количества ключевых слов
for query in queries:
    pass
