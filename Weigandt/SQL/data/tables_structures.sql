/*
    This script was adapted for PostgreSQL 13.
    It was run and tested in Ubuntu 18.04 LTS.
    There is no option to buy Oracle to pass this stage.

    I decide to bring changes in the structure of relations
    according to SQL_Test_Instructions.docx Assumptions section
    as I had understood them.
*/


-----------------------------------
-- Creating rpm_future_retail
-----------------------------------
CREATE TABLE IF NOT EXISTS rpm_future_retail
(
    future_retail_id         BIGINT PRIMARY KEY CHECK(future_retail_id > 0),
    item                     VARCHAR(20) NOT NULL,
    location                 INTEGER NOT NULL,
    action_date              DATE NOT NULL,
    selling_retail           NUMERIC(10, 4),
    selling_retail_currency  VARCHAR(3),
    selling_uom              VARCHAR(2)
    --UNIQUE (item, location, action_date)
);

-- Use the provided rpm_future_retail.sql file to insert data 
-- OR: select * from rpm_future_retail for update;
-- and then insert data manually from Excel file


-----------------------------------
-- Creating rpm_zone_future_retail
-----------------------------------
CREATE TABLE IF NOT EXISTS rpm_zone_future_retail
(
    zone_future_retail_id    BIGINT PRIMARY KEY CHECK(zone_future_retail_id > 0),
    item                     VARCHAR(20) NOT NULL,
    zone                     INTEGER NOT NULL,
    action_date              DATE NOT NULL,
    selling_retail           NUMERIC(10, 4),
    selling_retail_currency  VARCHAR(3),
    selling_uom              VARCHAR(2)
);

-- Use the provided rpm_zone_future_retail.sql file to insert data 
-- OR: select * from rpm_zone_future_retail for update;
-- and then insert data manually from Excel file 


-----------------------------------
-- Creating rpm_zone_location:
-----------------------------------
CREATE TABLE IF NOT EXISTS rpm_zone_location
(
    zone_id  BIGINT, 
    location INTEGER,
    UNIQUE(zone_id, location),
    FOREIGN KEY(zone_id) REFERENCES rpm_zone_future_retail(zone)
);

-- Use the provided rpm_zone_location.sql file to insert data 
-- OR: select * from rpm_zone_location for update;
-- and then insert data manually from Excel file
