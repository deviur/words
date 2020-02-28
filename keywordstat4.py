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
keywordstat4.py < yandex-stat-file.csv > rasult.csv
"""
from csv_handler import *
from table_handler import *

# Версия с использованием функций def
# TODO Добавить обработку аргументов командной строки
# TODO Добавить 'минус слова', их не учитывать при подсчёте показателей

VERSION = '0.3.0'


def main():
    querytable = load_table()

    querytable = add_totals_column(querytable)
    wordtable = split_queries_to_words(querytable)
    wordtable = sort_table(wordtable, sort_by='Total', reverse=True)

    unload_table(wordtable)


if __name__ == "__main__":
    main()
