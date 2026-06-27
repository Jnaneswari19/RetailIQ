USE retailiq;

INSERT INTO customers (customer_name, city, phone) VALUES
('Rahul Sharma','Hyderabad','9876543210'),
('Priya Reddy','Bangalore','9876543211'),
('Arjun Kumar','Chennai','9876543212'),
('Sneha Rao','Mumbai','9876543213'),
('Kiran Patel','Pune','9876543214');

INSERT INTO products (product_name, category, price) VALUES
('Laptop','Electronics',65000),
('Mouse','Electronics',700),
('Keyboard','Electronics',1500),
('Monitor','Electronics',12000),
('Printer','Electronics',9000);

INSERT INTO sales
(customer_id, product_id, quantity, sale_date, total_amount)
VALUES
(1,1,1,'2025-01-15',65000),
(2,2,3,'2025-02-12',2100),
(3,3,2,'2025-03-08',3000),
(4,4,1,'2025-04-10',12000),
(5,5,2,'2025-05-18',18000),
(1,2,2,'2025-06-05',1400),
(2,3,1,'2025-06-15',1500),
(3,4,1,'2025-06-20',12000),
(4,1,1,'2025-06-22',65000),
(5,2,5,'2025-06-25',3500);