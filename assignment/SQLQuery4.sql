CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    status INTEGER NOT NULL
);

INSERT INTO suppliers (supplier_id, name, city, status)
VALUES 
(1, 'Supplier A', 'New York', 10),
(2, 'Supplier B', 'Los Angeles', 20),
(3, 'Supplier C', 'Chicago', 25),
(4, 'Supplier D', 'Houston', 5),
(5, 'Supplier E', 'Phoenix', 30);

CREATE VIEW vw_high_status_suppliers AS
SELECT *
FROM suppliers
WHERE status > 15


SELECT * FROM vw_high_status_suppliers;