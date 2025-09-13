# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset
data = pd.read_csv('sales_data.csv')

# Show first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Check data types and missing values
print("\nDataset info:")
print(data.info())
print("\nMissing values per column:")
print(data.isnull().sum())

# Drop missing values (if any)
data = data.dropna()

# Task 2: Basic Data Analysis
print("\nBasic statistics of numerical columns:")
print(data.describe())

# Group by product to find average revenue
product_group = data.groupby('Product')['Revenue ($)'].mean()
print("\nAverage revenue per product:")
print(product_group)

# Task 3: Data Visualization

# 1. Line chart: Revenue over time
daily_sales = data.groupby('Date')['Revenue ($)'].sum()
daily_sales.plot(kind='line', marker='o', figsize=(8,5), title='Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.show()

# 2. Bar chart: Average revenue per product
product_group.plot(kind='bar', figsize=(8,5), title='Average Revenue per Product', color='skyblue')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.show()

# 3. Histogram: Quantity Sold distribution
data['Quantity Sold'].plot(kind='hist', bins=10, figsize=(8,5), title='Quantity Sold Distribution', color='lightgreen')
plt.xlabel('Quantity Sold')
plt.show()

# 4. Scatter plot: Revenue vs Quantity Sold
data.plot(kind='scatter', x='Quantity Sold', y='Revenue ($)', figsize=(8,5), title='Revenue vs Quantity Sold', color='red')
plt.show()
