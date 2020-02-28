#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Это модуль, который отвечает за загрузку и выгрузку csv-файла в список OrderedDict словарей и/или из него.

Каждый элемент списка соответсвует строке таблицы, ключи словаря соответствуют названиям столбцов таблицы,
а значения словаря соответствуют значениям ячеек таблицы.

Если имя файла не указывается, то соответвенно используется stdin и/или stdout.


>>> table = load_table('test.csv')
>>> len(table)
6

>>> unload_table(table,'result.csv')
6

"""


def load_table(filename=''):

    from csv import DictReader
    from sys import stdin

    f = open(filename, "r") if filename else stdin

    reader = DictReader(f)
    rows = [line for line in reader]
    return rows


def unload_table(table, filename=''):

    from csv import DictWriter
    from sys import stdout

    f = open(filename, "w") if filename else stdout

    writer = DictWriter(f, fieldnames=table[0].keys())
    writer.writeheader()
    writer.writerows(table)
    return len(table)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
