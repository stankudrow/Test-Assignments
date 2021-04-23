/*
  Some of constraints are arbitrary, therefore, unnecessary.
  The order of table creation matters.
  Any possible coincidences are random.
*/

-- Дилерские центры
CREATE TABLE IF NOT EXISTS Shop
(
  id SMALLSERIAL PRIMARY KEY CHECK (id > 0),
  name VARCHAR(50) NOT NULL
);

-- Производитель автомобиля
CREATE TABLE IF NOT EXISTS Manufacturer
(
  id SMALLSERIAL PRIMARY KEY CHECK (id >= 100),
  name VARCHAR(50) NOT NULL,
  country VARCHAR(50) NOT NULL
);

-- Модель автомобиля (марка? - brand or model?)
CREATE TABLE IF NOT EXISTS Mark
(
  id SMALLINT PRIMARY KEY CHECK (id > 0),
  name VARCHAR(50) NOT NULL,
  manufacturer_id SMALLINT REFERENCES Manufacturer(id) 
);

-- Выставленные на продожу машины (stock???)
CREATE TABLE IF NOT EXISTS Stock
(
  id SMALLSERIAL PRIMARY KEY CHECK (id > 0),
  shop_id SMALLINT NOT NULL REFERENCES Shop(id),
  mark_id SMALLINT NOT NULL REFERENCES Mark(id),
  quantity INT CHECK(quantity >= 0) DEFAULT 0
);

-- Populating relations

INSERT INTO Shop
VALUES
(2, 'Shop2'),
(5, 'Shop5'),
(11, 'Shop11'),
(7, 'Shop7'),
(3, 'Shop3'),
(2, 'Shop2'),
(12, 'Shop12') ON CONFLICT DO NOTHING;  -- if exists, then skip inserting
-- if, e.g., id violates check constraint, error arises and stops inserting


-- ISO-3166 - country codes
INSERT INTO Manufacturer
VALUES
(100, 'Honda', 'JAP'),
(101, 'Mazda', 'JAP'),
(102, 'Toyota', 'JAP'),
(200, 'KIA Motors', 'KOR'),
(202, 'Hyundai Motor Company', 'KOR'),
(300, 'Ford', 'US'),
(401, 'Volkswagen', 'GE'),
(402, 'Audi', 'GE') ON CONFLICT DO NOTHING;


INSERT INTO Mark
VALUES
(5, 'Accord', 100),
(6, 'Breeze', 100),
(7, 'Civic', 100),
(43, 'Santa Fe', 202),
(45, 'Ioniq', 202),
(53, 'Stinger', 200),
(55, 'Mohave', 200),
(52, 'Rio X', 200) ON CONFLICT DO NOTHING;


-- So one shop, one stock and vice versa? All right.
INSERT INTO Stock
(id, shop_id, mark_id, quantity)
VALUES
(22, 2, 5, 30),
(31, 5, 7, 56),
(47, 2, 5, 44),
(33, 2, 52, 38),
(19, 7, 45, 67),
(17, 12, 55, 13),
(15, 11, 43, 0),
(9, 3, 43, 7) ON CONFLICT DO NOTHING;
