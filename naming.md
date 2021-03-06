# Некоторые мысли по поводу названий сущностей в проекте.
Что делает программа и для чего она это делает?

Имеем яндекс таблицу (YandexTable) в csv формате с количеством кликов следующего вида.

|Query          |2020-02-10|2020-02-03 - 2020-02-09| ... |
| ------------- | --------:| ---------------------:| --- |
| vk api python |       2.0|                    8.0| ... |

(На самом деле, точно такая же таблица может быть для количества показов, для CTR и для средней позиции на странице.
Какие данные в таблице может знать только пользователь и то, если он только что загрузил эту таблицу. Что это будет
в рамках данного проекта получается не важно. Программа просто суммирует столбцы по каждой строке.)

Мы имеем яндекс таблицу с числовыми показателями поисковой выдачи яндекса по каждому запросу.
Показатель определяет пользователь в интерфейсе кабинета Яандекс.Вебмастер, перез загрузкой таблицы.
Это может быть Количество показов, либо количество кликов.

Программа просто подводит итог суммы показателя по каждому слову из запроса и выводит результат.
Результатом пусть будет файл с тем же именем, но с добавленным столбцом итогов.

Итак мы имеем,
**YandexTable** - таблица запросов с показателями поисковой выдачи Яндекса 
*Пожалуй, YandexTable - слишком абстактно. Здесь имеется ввиду табица с показателями запросов*

**QueryTable** - таблица с запросами и числовыми показателями их поисковой выдачи (Показы либо клики).

**WordTable** - таблица со словами и числовыми показателями их поисковой выдачи (либо показы, либо клики)

**YandexTable_rows** - строки таблицы

**YandexTable_cols** - столбцы таблицы

**LoadYandexTable** - загрузить таблицу запросов с показателями поисковой выдачи Яндекса

**UnloadYandexTable** - загрузить таблицу запросов с показателями поисковой выдачи Яндекса

**AddTotalCol** - добавить столбец итогов 

Нам понадобится загрузить csv-файл в память компьютера, а затем выгрузить результат. Пусть за это будет
отвечать модуль *csv_handler.py*. Файл загружается в список OrderedDict словарей, где каждый элемент списка
соответсвует строке таблицы, ключи словаря соответствуют названиям столбцов таблицы, а значения словаря 
соответствуют значениям ячеек таблицы.

Затем нам подадобится подвести итог суммы числовых показателей по каждому запросу.
Теперь нам понадобится сложить числовые значения в каждой строке таблицы и добавить новый столбец с итогом
За это будет отвечать функция *add_totals_column()*. Эта функция может быть универсальной, в том плане, что
столбец можно добавить в любую таблицу.

Сумму показателей по каждой строке (т.е. по каждому запросу) можно вывести в следующем виде.
 
|Query          |Total      |
| ------------- | ---------:|
| vk api python |       10.0| 

Нам понадобится разбить запрос на слова *split_query()* и расчитать сумму показателей по каждому слову из запроса.
Преобразовать таблицу с показателями по запросам в таблицу с показателями по словам *split_queries_to_words()*.

~~Возможно, *split_to_words()*, а то что разбиваются запросы можно понять по параметрам. 
Например, *split_to_words(query_table)*. Вообще не очень понятно. Как будто по словам разбиваем таблицу, 
а не запрос.~~ Как с этим быть? Можно было бы так: *split_to_words(queries)*. Так понятней! 
А вот так, ещё лучше: *word_table = split_to_words(queries)* 

Тут мы делаем что-то с таблицами в памяти, добавляем столбцы, удаляем столбцы и преоброазуем таблицу.
Пусть за это будет отвечать модуль *table_handler.py*.

 



Варианты, что делает программа:
0. Подводит итог по количеству кликов по каждому запросу.
0. Считает общее количество кликов по каждому запросу  (CountTotalClicks).
0. Добавляет итоговой столбец к таблице запросов (csv.YandexTable.AddTotalColumn).
0. Выводит статистику запросов (QueryStat).
0. Преобразует таблицу кликов (ClicksTable)
0. Выводит статистку по каждому поисковуму запросу (SearchQuery)
0. 
