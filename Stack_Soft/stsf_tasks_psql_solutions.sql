/*
The scheme and tasks were tested in PostgreSQL version 13.
*/

CREATE TABLE Rate
(
  service_id SMALLINT CHECK (service_id > 0),
  price      SMALLINT CHECK (price >= 0),
  start_date DATE, -- mm.dd.yyyy format
  
  UNIQUE(service_id, start_date)
);


INSERT INTO Rate VALUES
(1, 10,  '01.01.2020'),
(5, 9,   '07.01.2020'),
(5, 10,  '07.02.2020'),
(2, 7,   '07.03.2020'),
(3, 18,  '12.03.2020'),
(5, 12,  '01.04.2021'),
(1, 14,  '01.04.2021'),
(4, 11,  '01.04.2021'),
(3, 12,  '01.05.2021'),
(2, 9,   '01.05.2021'),
(5, 10,  '01.05.2021'),
(4, 13,  '02.05.2021'),
(3, 12,  '02.05.2021'),
(1, 70,  '03.26.2021'),
(1, 57,  '02.12.2021'),
(2, 60,  '03.26.2021'),
(3, 73,  '03.26.2021'),
(3, 80,  '12.17.2021'),
(4, 90,  '03.26.2021'),
(4, 96,  '12.29.2021'),
(5, 100, '03.26.2021'),
(5, 120, '03.27.2021'),
(5, 101, '12.26.2021');


/* Tasks section */


-- The first task.

SELECT * FROM Rate
WHERE service_id = 3 AND start_date <= NOW()
ORDER BY start_date DESC LIMIT 1;

-- The second task.

SELECT service_id, MIN(price) as min_price
FROM Rate
GROUP BY service_id
ORDER BY 2 DESC;

-- The third task.

SELECT MIN(service_id), MAX(price)
FROM Rate
JOIN (SELECT service_id as sid, MAX(start_date) as sdate
      FROM Rate
      WHERE start_date <= NOW() - INTERVAL '1 DAY'
      GROUP BY service_id) AS onyester
ON service_id = sid AND start_date = sdate
GROUP BY price;
