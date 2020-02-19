#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Модуль получения словаря запросов (dict=>{запрос: кол-во кликов}) из OrderedDict-словаря

>>> from input_csv import input_csv
>>> result = input_csv('test.csv')
>>> queries = get_queries(result)
>>> sum(queries.values())
59.0
"""


def get_queries(dict_):

    queries = {}
    for line in dict_:
        for key, value in line.items():
            if key == 'Query':
                query = value
                clicks = 0
            else:
                clicks += float(value)

        queries.update({query: clicks})

    return queries


if __name__ == "__main__":
    import doctest
    doctest.testmod()
