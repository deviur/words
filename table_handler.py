#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Модуль для обработки таблиц на питоне.
1. Добавляет столбец итогов.
2.

>>> from csv_handler import load_table
>>> table = load_table('test.csv')
>>> len(table)
6

>>> table = add_totals_column(table)
>>> sum([row['Total'] for row in table])
59.0

>>> table = split_queries_to_words(table)
>>> sum([row['Total'] for row in table])
145.0

>>> table = sort_table(table, 'Total')
>>> table[0]['Word']
'на'
"""


def add_totals_column(table):

    for row in table:
        for column, value in row.items():
            if column == 'Query':
                clicks = 0
            else:
                clicks += float(value)

        row.update({'Total': clicks})

    return table


def split_queries_to_words(querytable):

    from re import findall
    from collections import OrderedDict

    wordtable = {}

    for row in querytable:
        words = findall('[a-zA-Zа-яА-ЯёЁ]+', row['Query'])
        for word in words:
            if word in wordtable:
                wordtable[word]['Total'] += row['Total']
            else:
                wordtable[word] = OrderedDict(Word=word, Total=row['Total'])
    return [wordrow for wordrow in wordtable.values()]


def sort_table(table, sort_by, reverse=False):
    table.sort(key=lambda i: i[sort_by])
    table.reverse() if reverse else None
    return table


if __name__ == "__main__":
    import doctest
    doctest.testmod()
