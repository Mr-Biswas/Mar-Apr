----------------------------------------TABLE CREATION---------------------------------
CREATE TABLE Customer (
    CustomerID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    State VARCHAR(50)
);

----------------------------------------TABLE CREATION---------------------------------
CREATE TABLE Transactions (
    TransactionID SERIAL PRIMARY KEY,
    Status VARCHAR(50),
    Mode VARCHAR(50),
    SaleDate DATE,
    Month VARCHAR(20),
    CustomerID INT,
    Gender VARCHAR(20),
    Age INT,
    AgeGroup VARCHAR(20),
    Category VARCHAR(50),
    ProductName VARCHAR(100),
    Region VARCHAR(20),
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    COGS DECIMAL(10, 2),
    TotalSales DECIMAL(10, 2),
    CONSTRAINT fk_customer
        FOREIGN KEY (CustomerID)
        REFERENCES Customer(CustomerID)
);

---------------------------------------------QUERING THE TABLE------------------
Select *
From Customer
limit 10;

---------------------------------------------QUERING THE TABLE------------------
Select *
From Transactions;

---------*****DATA EXPLORATION AND CLEANING

---COUNT TOTAL RECORDS AVAILABLE
Select COUNT(*)
From Transactions;

Select COUNT(*)
From Customer;

Select Count(Distinct(CustomerID))
From Transactions;

SELECT DISTINCT category FROM Transactions;


SELECT * FROM Transactions
WHERE 
       TransactionID IS NULL 
	OR Status IS NULL 
	OR Mode IS NULL 
	OR SaleDate IS NULL 
	OR Month IS NULL 
	OR CustomerID IS NULL 
	OR Gender IS NULL 
	OR Age IS NULL 
	OR AgeGroup IS NULL
	OR Category IS NULL
	OR ProductName IS NULL
	OR Region IS NULL
	OR Quantity IS NULL
	OR UnitPrice IS NULL
	OR TotalSales IS NULL;

---*********DATA ANALYSIS AND FINDINGS

--SQL query to retrieve all columns for sales made on '2022-11-04

SELECT *
FROM Transactions
WHERE SaleDate = '2022-04-11';

-- SQL query to retrieve all transactions where the category is 'Clothing' and the quantity sold is more than 3 in the month of April-2022:
SELECT *
FROM Transactions
WHERE 
    category = 'Clothing'
    AND 
    TO_CHAR(SaleDate, 'YYYY-MM') = '2022-04'
    AND
    quantity >= 3
--SQL query to calculate the total sales (total_sale) for each category.
SELECT 
    Category,
    SUM(TotalSales) as net_sale,
    COUNT(*) as total_orders
FROM Transactions
GROUP BY 1

--SQL query to find the average age of customers who purchased items from the 'Electronics' category.
SELECT
    ROUND(AVG(Age), 2) as avg_age
FROM Transactions
WHERE Category = 'Electronics';

--SQL query to find all transactions where the total_sale is greater than 1000.
SELECT * FROM Transactions
WHERE TotalSales > 1000;
SELECT COUNT(*) FROM Transactions
WHERE TotalSales > 1000;

--SQL query to find the total number of transactions (transaction_id) made by each gender in each category.
SELECT 
    Category,
    Gender,
    COUNT(*) as total
FROM Transactions
GROUP BY 
    category,gender;

--SQL query to find the number of unique customers who purchased items from each category.
SELECT 
    Category,    
    COUNT(DISTINCT CustomerID) as Unique
FROM Transactions
GROUP BY Category;

-- Sql query to find State vs Total sales records.
SELECT 
    c.State, 
    SUM(t.TotalSales) AS TotalSales
FROM 
    Transactions t
JOIN 
    Customer c ON t.CustomerID = c.CustomerID
GROUP BY 
    c.State
ORDER BY 
    TotalSales DESC
limit 5;

-- Sql query to find State vs Total Quantity records.

SELECT 
    c.State, 
    COUNT(t.TransactionID) AS TotalTransactions
FROM 
    Transactions t
JOIN 
    Customer c ON t.CustomerID = c.CustomerID
GROUP BY 
    c.State
ORDER BY 
    TotalTransactions DESC;

-- Sql query to find customer and their category  vs purchasing power record.
SELECT 
    c.State,
	t.Gender,
    COUNT(t.TransactionID) AS TotalTransactions
FROM 
    Transactions t
JOIN 
    Customer c ON t.CustomerID = c.CustomerID
GROUP BY 
    c.State,
	t.Gender
ORDER BY 
    TotalTransactions DESC;

--SQL query to calculate the average sale for each month. Find out best selling month in each year.

SELECT 
       year,
       month,
    avg_sale
FROM 
(    
SELECT 
    EXTRACT(YEAR FROM SaleDate) as year,
    EXTRACT(MONTH FROM SaleDate) as month,
    ROUND(AVG(TotalSales),2) as avg_sale,
    RANK() OVER(PARTITION BY EXTRACT(YEAR FROM SaleDate) ORDER BY AVG(TotalSales) DESC) as rank
FROM Transactions
GROUP BY 1, 2
) as t1
WHERE rank = 1;

--END OF PROJECT


