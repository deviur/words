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
import re
import sys

VERSION = '0.1'

input_csv = csv.DictReader(sys.stdin)
all_words = {}

# Подсчёт количества кликов (clicks) на сайт по каждому запросу (query).
queries = []
for line in input_csv:
    for key, value in line.items():
        if key == 'Query':
            query = value
            clicks = 0
        else:
            clicks += float(value)

    queries.append({'Query': query, 'Clicks': clicks})

print(queries)
# Результат:
# [{'Query': 'Несколько винипухов', 'Clicks': 18.0}, {'Query': 'Винипухи сильнее всех', 'Clicks': 13.0},
# {'Query': 'без винипухов никуда', 'Clicks': 10.0}, {'Query': 'долой винипухов', 'Clicks': 7.0},
# {'Query': 'сильнее винипуха', 'Clicks': 7.0}, {'Query': 'всех на винипухов', 'Clicks': 4.0}]

# TODO Сделать сортировку. Как?

# Получить список слов из запросов и сумму кликов
all_words = {}
for query in queries:
    # PEP 8: invalid escape sequence '\w' For us it means that flake8 is upset
    words = re.findall('\w+', query['Query'])

    for word in words:
        if word in all_words:
            all_words[word]['Query'].append(query['Query'])
            all_words[word]['Clicks'] += query['Clicks']
        else:
            all_words[word] = {'Clicks': query['Clicks'], 'Query': [query['Query']]}

print(all_words)
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
