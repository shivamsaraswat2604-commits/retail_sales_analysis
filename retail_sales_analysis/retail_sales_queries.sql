
-- =====================================================
-- Retail Sales Performance - SQL Analysis Queries
-- =====================================================

-- 1. Calculate Monthly Revenue
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS SalesMonth,
    SUM(TotalRevenue) AS MonthlyRevenue
FROM retail_transactions
GROUP BY SalesMonth
ORDER BY SalesMonth;

-- 2. Identify Top-Selling Products
SELECT 
    ProductName,
    Category,
    SUM(Quantity) AS TotalUnitsSold,
    SUM(TotalRevenue) AS TotalRevenue
FROM retail_transactions
GROUP BY ProductName, Category
ORDER BY TotalRevenue DESC
LIMIT 5;

-- 3. Analyze Regional Trends & Order Volumes
SELECT 
    Region,
    COUNT(TransactionID) AS OrderVolume,
    SUM(TotalRevenue) AS RegionalRevenue,
    AVG(TotalRevenue) AS AvgOrderValue
FROM retail_transactions
GROUP BY Region
ORDER BY RegionalRevenue DESC;
