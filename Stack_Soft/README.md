# Описание

Задание на должость PL/SQL младшего разработчика.


## Исходные данные

Таблица Rate:

* service_id - отождествитель (идентификатор) услуги;

* price - цена услуги;

* start_date - дата начала действия цены на услугу.

Суть таблицы: с некоторой даты А действует цена В. Могут быть цены, действующие в будущем.


## Задания

1. Написать запрос, возвратящий действующую цену для услуги с id равным 3 на текущую дату.

2. Написать запрос, возвратящий список всех услуг с их когда-либо существ(ующ/овавш)ими наименьшими (минимальными) ценами. Вернуть упорядоченный по убыванию цены запрос.

3. Написать запрос, возвратящий id услуги с наибольшей (максимальной) ценой, действовавшей на вчера. Если услуг несколько, вернуть услуги с наименьшими отождествителями (id).
