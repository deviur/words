#! /bin/sh
"""true"
if command -v python3 > /dev/null; then
  exec python3 "$0" "$@"
else
  exec python "$0" "$@"
fi
exit $?

Модуль получения словаря запросов (dict=>{запрос: кол-во кликов}) из OrderedDict-словаря

>>> queries = {'порядок, слова': 10, '10 по порядку слова': 7, 'порядок & беспорядок': 5}
>>> keywords = get_keywords(queries)
>>> len(keywords)
5

>>> sum(keywords.values())
51
"""


def get_keywords(queries):
    from re import findall
    all_words = {}
    for query, clicks in queries.items():
        words = findall('[a-zA-Zа-яА-ЯёЁ]+', query)
        for word in words:
            if word in all_words:
                all_words[word] += clicks
            else:
                all_words[word] = clicks
    return all_words


if __name__ == "__main__":
    import doctest
    doctest.testmod()
