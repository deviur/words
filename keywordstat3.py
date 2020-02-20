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
keywordstat3.py < yandex-stat-file.csv > output.csv
"""
import input_csv
import querystat
import wordstat

# Версия с использованием функций def
# TODO Добавить тест скорости обработки
# TODO Добавить тест использования памяти
# TODO Убрать лишние действия со словарями
# TODO Добавить обработку аргументов командной строки
# TODO Сделать код более читабельным

VERSION = '0.2.1'


# Функция: Сортировка словаря по значению
# Функция возвращает упорядоченный список кортежей
def sort_dict_value(dict_, reverse=False):
    list_ = list((dict_.items()))
    list_.sort(key=lambda i: i[1])
    list_.reverse() if reverse else None
    return list_


def output_csv(list_):
    print('Word, Total')
    for key, value in list_:
        print(f"{key}, {value}")


def main():
    # Загрузить csv-файл для обработки в упорядоченный словарь
    table = input_csv.input_csv()

    # Подсчитать общее количество кликов по каждому запросу
    table = querystat.get_queries(table)

    # Подсчитать общее количество кликов по каждому ключевому слову
    table = wordstat.get_keywords(table)

    # Сортировка словаря по значению
    keywords = sort_dict_value(table, reverse=True)

    # Вывод результатов
    output_csv(keywords)


if __name__ == "__main__":
    main()
