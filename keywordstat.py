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

# Получить список слов из запросов и сумму кликов
num = 1
all_words = {}
for query in queries:
    # PEP 8: invalid escape sequence '\w' For us it means that flake8 is upset
    words = re.findall('\w+', query['Query'])

    print(num, words)
    num += 1
    for word in words:
        if word in all_words:
            print(f"word in all_words: {word}: {all_words[word]['Query']} + {query['Query']}")
            all_words[word]['Query'].append(query['Query'])
            all_words[word]['Clicks'] += query['Clicks']
        else:
            print(f"Новый эллемент: \n {word} -> {query['Clicks']} = {query['Query']}")
            all_words[word] = {'Clicks': query['Clicks'], 'Query': [query['Query']]}

print(all_words)

# TODO Убрать DEBUG-код. Подумать как упростить вывод результата.
