#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Модуль для загрузки csv-файла в список OrderedDict-словарей. csv-файл берётся со страницы Яндекс.Вебмастер.
Файл содержит информацию о количестве кликов по каждому запросу в разные периоды в слудующем формате:

|Query          |2020-02-10|2020-02-03 - 2020-02-09| ... |
| ------------- | --------:| ---------------------:| --- |
|Запрос         |       2.0|                    8.0| ... |
| ...           |       ...|                    ...| ... |,

где количество столбцов и строк может быть произвольным.

Получить файл можно на этой странице:
https://webmaster.yandex.ru/site/https:denislepeshkin.ru:443/search/statistics/?specialGroup=TOP_3000_QUERIES&deviceType=ALL_DEVICES&indicator=total-clicks-count&dateFrom=2020-01-13T00%3A00%3A00%2B03%3A00&dateTo=2020-02-13T23%3A59%3A59%2B03%3A00&period=DAY&orderBy=total-shows-count&orderDirection=desc

На выходе будет список упорядочненных словарей в следующем виде:
[OrderedDict([('Query', 'Несколько винипухов'), (' 2020-01-10', ' 10'), (' 2020-02-10', ' 8'), ...]), ...]


Тесты:

>>> result = input_csv('test.csv')
>>> len(result)
6

>>> result[2]['Query']
'без винипухов никуда'
"""


# Функция: Загрузка csv-файла в список упорядоченных словарей OrderedDict.
# Фукция возвращает список упорядоченных словарей.
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
