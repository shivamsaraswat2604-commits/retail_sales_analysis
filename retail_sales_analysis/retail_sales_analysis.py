"""
=============================================================================
Project Name: Retail Sales Performance Dashboard & SQL Analytics
Author: Shivam Saraswat
Description: 
    Generates a synthetic dataset of 100 retail transactions, cleans and 
    structures the data for SQL querying and Power BI dashboard consumption, 
    and outputs analytical metrics (monthly revenue, top-selling products, regional trends).
=============================================================================
"""

import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# ==========================================
# 1. GENERATE RETAIL TRANSACTIONS DATASET
# ==========================================
print('[INFO] Generating retail transactions dataset...')
n_transactions = 100

products = [
    {'ProductID': 'P001', 'ProductName': 'Wireless Mouse', 'Category': 'Electronics', 'Price': 25.00},
    {'ProductID': 'P002', 'ProductName': 'Mechanical Keyboard', 'Category': 'Electronics', 'Price': 75.00},
    {'ProductID': 'P003', 'ProductName': 'HD Monitor', 'Category': 'Electronics', 'Price': 150.00},
    {'ProductID': 'P004', 'ProductName': 'Ergonomic Office Chair', 'Category': 'Furniture', 'Price': 200.00},
    {'ProductID': 'P005', 'ProductName': 'Standing Desk', 'Category': 'Furniture', 'Price': 350.00},
    {'ProductID': 'P006', 'ProductName': 'USB-C Hub', 'Category': 'Accessories', 'Price': 40.00},
    {'ProductID': 'P007', 'ProductName': 'Desk Lamp', 'Category': 'Furniture', 'Price': 45.00}
]

# Randomly select products for 100 transactions
selected_products = np.random.choice(products, size=n_transactions)
regions = ['North', 'South', 'East', 'West']

data = []
for i, prod in enumerate(selected_products, start=1):
    trans_date = pd.to_datetime('2025-01-01') + pd.to_timedelta(np.random.randint(0, 365), unit='D')
    quantity = np.random.randint(1, 5)
    total_revenue = quantity * prod['Price']
    
    data.append({
        'TransactionID': f'TXN-{i:03d}',
        'Date': trans_date.strftime('%Y-%m-%d'),
        'Month': trans_date.strftime('%B'),
        'ProductID': prod['ProductID'],
        'ProductName': prod['ProductName'],
        'Category': prod['Category'],
        'Quantity': quantity,
        'UnitPrice': prod['Price'],
        'TotalRevenue': total_revenue,
        'Region': np.random.choice(regions)
    })

df_sales = pd.DataFrame(data)

# Save dataset to CSV for Excel / SQL import
df_sales.to_csv('retail_sales_data.csv', index=False)
print('[SUCCESS] Dataset generated and saved as "retail_sales_data.csv".\n')


# ==========================================
# 2. SQL ANALYTICAL QUERIES (SIMULATED VIA PANDAS)
# ==========================================
print('============================================')
print('SQL PERFORMANCE METRICS & ANALYSIS')
print('============================================')

# A. Monthly Revenue Calculation
print('\n1. Monthly Revenue Breakdown:')
monthly_revenue = df_sales.groupby('Month')['TotalRevenue'].sum().reset_index()
print(monthly_revenue.to_string(index=False))

# B. Top-Selling Products by Revenue
print('\n2. Top-Selling Products by Total Revenue:')
top_products = df_sales.groupby(['ProductName', 'Category'])['TotalRevenue'].sum().reset_index()
top_products = top_products.sort_values(by='TotalRevenue', ascending=False).head(5)
print(top_products.to_string(index=False))

# C. Regional Performance Trends
print('\n3. Regional Sales Performance:')
regional_trends = df_sales.groupby('Region').agg(
    TotalRevenue=('TotalRevenue', 'sum'),
    TotalOrders=('TransactionID', 'count')
).reset_index()
print(regional_trends.to_string(index=False))
print('============================================\n')


# ==========================================
# 3. SQL CODE SCRIPT FOR GITHUB REPOSITORY
# ==========================================
sql_code = """
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
"""

with open('retail_sales_queries.sql', 'w') as f:
    f.write(sql_code)

print('[SUCCESS] SQL query template saved as "retail_sales_queries.sql".')