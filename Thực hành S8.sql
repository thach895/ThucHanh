CREATE DATABASE SalesManagement;
USE SalesManagement;

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    birth_date DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    customer_type VARCHAR(20) DEFAULT 'Normal'
);

CREATE TABLE Category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(150) NOT NULL,
    price DECIMAL(12,2) NOT NULL CHECK (price > 0),
    stock INT NOT NULL CHECK (stock >= 0),
    category_id INT NOT NULL,

    FOREIGN KEY (category_id)
    REFERENCES Category(category_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) DEFAULT 'Pending',

    FOREIGN KEY (customer_id)
    REFERENCES Customer(customer_id)
);

CREATE TABLE Order_Detail (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(12,2) NOT NULL CHECK (unit_price > 0),

    FOREIGN KEY (order_id)
    REFERENCES Orders(order_id),

    FOREIGN KEY (product_id)
    REFERENCES Product(product_id)
);

INSERT INTO Customer(full_name, gender, birth_date, email, phone, address, customer_type)
VALUES
('Nguyen Van A', 'M', '2002-05-10', 'vana@gmail.com', '0901111111', 'Ha Noi', 'VIP'),
('Tran Thi B', 'F', '1999-09-15', 'thib@gmail.com', '0902222222', 'Da Nang', 'Normal'),
('Le Van C', 'M', '2005-01-20', 'vanc@gmail.com', '0903333333', 'HCM', 'VIP'),
('Pham Thi D', 'F', '2001-12-11', 'thid@gmail.com', '0904444444', 'Can Tho', 'Normal'),
('Hoang Van E', 'M', '1998-03-25', 'vane@gmail.com', '0905555555', 'Hai Phong', 'VIP');

INSERT INTO Category(category_name, description)
VALUES
('Dien tu', 'Cac thiet bi dien tu'),
('Thoi trang', 'Quan ao va phu kien'),
('Gia dung', 'Do dung gia dinh'),
('Sach', 'Sach giao khoa va tieu thuyet'),
('The thao', 'Dung cu the thao');

INSERT INTO Product(product_name, price, stock, category_id)
VALUES
('Laptop Dell', 25000000, 10, 1),
('iPhone 15', 30000000, 15, 1),
('Ao Hoodie', 500000, 50, 2),
('May Giat', 12000000, 8, 3),
('Sach SQL', 200000, 100, 4),
('Giay The Thao', 1500000, 25, 5),
('Tai nghe Bluetooth', 2000000, 20, 1);

INSERT INTO Orders(customer_id, order_date, status)
VALUES
(1, '2026-01-10', 'Completed'),
(2, '2026-02-15', 'Completed'),
(1, '2026-03-01', 'Pending'),
(3, '2026-03-20', 'Completed'),
(5, '2026-04-01', 'Cancelled');

INSERT INTO Order_Detail(order_id, product_id, quantity, unit_price)
VALUES
(1, 1, 1, 25000000),
(1, 7, 2, 2000000),
(2, 3, 3, 500000),
(3, 2, 1, 30000000),
(4, 5, 2, 200000);

UPDATE Product
SET price = 28000000
WHERE product_name = 'Laptop Dell';

UPDATE Customer
SET email = 'newemail@gmail.com'
WHERE customer_id = 2;

DELETE FROM Order_Detail
WHERE order_detail_id = 5;

SELECT
    full_name AS HoTen,
    email AS Email,
    CASE
        WHEN gender = 'M' THEN 'Nam'
        WHEN gender = 'F' THEN 'Nu'
    END AS GioiTinh
FROM Customer;

SELECT
    full_name,
    YEAR(NOW()) - YEAR(birth_date) AS age
FROM Customer
ORDER BY age ASC
LIMIT 3;

SELECT
    o.order_id,
    c.full_name,
    o.order_date,
    o.status
FROM Orders o
INNER JOIN Customer c
ON o.customer_id = c.customer_id;

SELECT
    c.category_name,
    COUNT(p.product_id) AS total_products
FROM Category c
INNER JOIN Product p
ON c.category_id = p.category_id
GROUP BY c.category_id, c.category_name
HAVING COUNT(p.product_id) >= 2;

SELECT
    product_name,
    price
FROM Product
WHERE price >
(
    SELECT AVG(price)
    FROM Product
);

SELECT
    full_name,
    email
FROM Customer
WHERE customer_id NOT IN
(
    SELECT customer_id
    FROM Orders
);

SELECT
    c.category_name,
    SUM(od.quantity * od.unit_price) AS total_revenue
FROM Category c
INNER JOIN Product p
ON c.category_id = p.category_id
INNER JOIN Order_Detail od
ON p.product_id = od.product_id
GROUP BY c.category_id, c.category_name
HAVING SUM(od.quantity * od.unit_price) >
(
    SELECT AVG(category_revenue) * 1.2
    FROM
    (
        SELECT
            SUM(od.quantity * od.unit_price) AS category_revenue
        FROM Category c
        INNER JOIN Product p
        ON c.category_id = p.category_id
        INNER JOIN Order_Detail od
        ON p.product_id = od.product_id
        GROUP BY c.category_id
    ) AS revenue_table
);

SELECT
    p.product_name,
    p.price,
    c.category_name
FROM Product p
INNER JOIN Category c
ON p.category_id = c.category_id
WHERE p.price =
(
    SELECT MAX(p2.price)
    FROM Product p2
    WHERE p2.category_id = p.category_id
);

SELECT full_name
FROM Customer
WHERE customer_type = 'VIP'
AND customer_id IN
(
    SELECT customer_id
    FROM Orders
    WHERE order_id IN
    (
        SELECT order_id
        FROM Order_Detail
        WHERE product_id IN
        (
            SELECT product_id
            FROM Product
            WHERE category_id =
            (
                SELECT category_id
                FROM Category
                WHERE category_name = 'Dien tu'
            )
        )
    )
);