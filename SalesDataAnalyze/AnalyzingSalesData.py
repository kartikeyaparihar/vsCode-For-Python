import pandas as pd
import numpy as np

dict1 = {"name": ['kartik' , 'yash' , 'parth' , 'ansh'],
        "marks": [100,64,78,55],
         "place": ['indore','bhpl','indore', 'bhpl']}
df = pd.DataFrame(dict1)
df.to_csv('sales_data.csv')
# Load the data
df = pd.read_csv('sales_data.csv')

# Clean the data
df.dropna(inplace=True)

# Compute total revenue
df['Revenue'] = df['Price'] * df['Quantity_Sold']

# Total Sales per Month
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Revenue'].sum()

# Top Selling Products
top_products = df.groupby('Product_Name')['Revenue'].sum().sort_values(ascending=False).head(10)

# Category-wise Sales
category_sales = df.groupby('Category')['Revenue'].sum()

# Customer Age Groups
df['Age_Group'] = pd.cut(df['Customer_Age'], bins=[0, 20, 40, 60, 80], labels=['0-20', '21-40', '41-60', '61-80'])
age_group_sales = df.groupby('Age_Group')['Revenue'].sum()

# Gender-based Analysis
gender_sales = df.groupby('Customer_Gender')['Revenue'].sum()

# Display results
print("Monthly Sales:\n", monthly_sales)
print("Top Selling Products:\n", top_products)
print("Category-wise Sales:\n", category_sales)
print("Age Group Sales:\n", age_group_sales)
print("Gender-based Sales:\n", gender_sales)