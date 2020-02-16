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
