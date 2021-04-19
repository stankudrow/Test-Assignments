/*
Задача 1.

С учетом приведенной схемы БД автомобильного дилера с таблицами stock (выставленные на продажу машины), shop (дилерские центры), mark (модели), manufacturer (производитель автомобилей), вывести одним запросом всех производителей автомобилей (manufacturer.name), указав сколько конкретных машин выставлено на продажу в каждом дилерском центре для этого производителя в порядке убывания. Также учитывать, что для некоторых производителей может не быть записей в таблице stock, при этом данные производители также должны присутствовать в итоговой выборке.
*/

SELECT mf.name manufacturer, mk.name brand, sh.name, st.quantity quantity
FROM Stock AS st JOIN Mark AS mk ON st.mark_id = mk.id
JOIN Shop AS sh ON st.shop_id = sh.id
RIGHT JOIN Manufacturer AS mf ON mk.manufacturer_id = mf.id
ORDER BY quantity DESC NULLS LAST;


/*
Задача 2-1.

Вывести суммарное количество выставленных на продажу машин японских производителей (manufacturer.country = 'JAP') для каждого дилерского центра.
*/

SELECT sh.name, SUM(st.quantity)
FROM Stock AS st JOIN Mark AS mk ON st.mark_id = mk.id
JOIN Shop AS sh ON st.shop_id = sh.id
RIGHT JOIN Manufacturer AS mf ON mk.manufacturer_id = mf.id
WHERE UPPER(mf.country) = 'JAP'
GROUP BY sh.name;


/*
Задача 2-2.

Вывести список моделей (mark.name) с указанием их производителя (manufacturer.name), которых нет на складах. Учитывать также те модели, по которым на текущий момент нет записей в таблице stock.
*/


/*
Задача 2-3.

Вывести для всех дилерских центров те модели (mark.name), у которых суммарное количество выставленных на продажу экземпляров больше 10 (stock.quantity). В этом же запросе для каждой модели указать центр (shop.name), в котором находится наибольшее количество моделей (если таких несколько, то отсортировать по имени центра в алфавитном порядке).
*/
