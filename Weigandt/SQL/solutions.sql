/*

Task 1.

Find duplicate records in RPM_FUTURE_RETAIL.
The record is a duplicate if an item/location/action_date combination exists (prices can differ):

    a. Write a query to return all duplicated records.

    b. Delete duplicate records, so that item/location/action_date will be unique.
*/

-- Task 1a.
SELECT item, location, action_date, COUNT(*)
FROM rpm_future_retail
GROUP BY item, location, action_date
HAVING COUNT(*) > 1
ORDER BY 1 DESC, 2 DESC, 3 DESC;  -- unnecessary ordering

-- Task 1b. - ????????
CREATE TABLE rfr AS (SELECT DISTINCT * FROM rpm_future_retail);
DROP TABLE rpm_future_retail;
ALTER TABLE rfr RENAME TO rpm_future_retail;

/*

Task 2.

Write a query to find all item/zone combinations in rpm_zone_future_retail
for which there are no pricing data exists at the location level (rpm_future_retail).
Note that locations linked to each zone can be obtained from rpm_zone_location table,
e.g.: zone: 1 = locations: 2302, 3040, … etc).
*/

SELECT rzfr.item, rzfr.zone
FROM rpm_zone_future_retail AS rzfr
JOIN rpm_zone_location AS rzl ON rzfr.zone = rzl.zone_id
JOIN rpm_future_retail AS rfr ON rzl.location = rfr.location;
WHERE rzfr.selling_retail NOT IN (SELECT selling_retail
                                  FROM rpm_future_retail
                                  GROUP BY 1)
GROUP BY 1, 2
ORDER BY 1;


/*

Task 3.

Write a query that will return current and previous selling retail prices (preceding action_date)
for each item/location combination and the difference between current and previous prices.

Hint: you might consider (not mandatory) using LEAD/LAG function to retrieve previous prices
and CASE function to compute the differences if previous prices exist,
otherwise, return null or 0 on your choice (optional).
*/



/*

Task 4.

Assuming that the current date in the system is today:

    a) Find the price for each item at each location on the current date.
       Since there are many prices for the same item/location combination,
       use the selling_retail values closest to the current  date,
       meaning latest action_date which is  <= current date).

    b) Find the differences in the prices between zone 1 and 2
       for all items on the current date.
*/
