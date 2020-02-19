#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Модуль для загрузки csv-файла в OrderedDict-словарь. csv-файл берётся со страницы Яндекс.Вебмастер.
Файл содержит информацию о количестве кликов по каждому запросу в разные периоды

Получить файл можно на этой странице:
https://webmaster.yandex.ru/site/https:denislepeshkin.ru:443/search/statistics/?specialGroup=TOP_3000_QUERIES&deviceType=ALL_DEVICES&indicator=total-clicks-count&dateFrom=2020-01-13T00%3A00%3A00%2B03%3A00&dateTo=2020-02-13T23%3A59%3A59%2B03%3A00&period=DAY&orderBy=total-shows-count&orderDirection=desc

>>> result = input_csv('test.csv')
>>> len(result)
6

>>> result[2]['Query']
'без винипухов никуда'

>>> result = input_csv()
>>> result

"""


# Функция: Загрузка csv-файла в упорядоченный словарь.
# Фукция возвращает упорядоченный словарь.
def input_csv(filename=''):

    from csv import DictReader
    from sys import stdin

    f = open(filename, "r") if filename else stdin

    reader = DictReader(f)
    entries = [line for line in reader]
    return entries


if __name__ == "__main__":
    import doctest
    doctest.testmod()