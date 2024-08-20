import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv(r"C:\Users\hp\Desktop\297 FINAL DATA ANALYTICS PROJECT\Top 500 Companies - India.csv")
#Checking columns
df.columns
#Total number of rows and columns
df.shape
#Complete information about the dataset
df.info()
#Checking duplicate values
df.duplicated().sum()
#Checking null values
df.isnull().sum()
#Removing unncessary column
df = df.drop('Unnamed: 4', axis =1)
#Handling missing values by dropping rows with missing values
df = df.dropna()
#Let's check our dataset now!
df.isnull().sum()
#Statistical description
df.describe()
# Calculate Profit Margin
df['Profit Margin'] = df['Mar Cap - Crore'] / df['Sales Qtr - Crore']
# Calculate Market Share
total_market_sales = df['Sales Qtr - Crore'].sum()
df['Market_Share'] = (df['Sales Qtr - Crore'] / total_market_sales) * 10
# Correlation matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
# Key Metrics
mean_market_cap = df['Mar Cap - Crore'].mean()
median_market_cap = df['Mar Cap - Crore'].median()
total_sales = df['Sales Qtr - Crore'].sum()
print(f"Mean Market Capitalization: {mean_market_cap}")
print(f"Median Market Capitalization: {median_market_cap}")
print(f"Total Sales: {total_sales}"
# Visualize Market Capitalization
sns.histplot(df['Mar Cap - Crore'], kde=True)
plt.title('Market Capitalization Distribution')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Frequency')
plt.show()
# Scatter plot of Market Cap vs. Sales
plt.scatter(df['Mar Cap - Crore'], df['Sales Qtr - Crore'])
plt.title('Market Capitalization vs. Sales')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Sales (Crore)')
plt.show()
# Sort the dataset by market capitalization in descending order
sorted_data = df.sort_values('Mar Cap - Crore', ascending=False)
# Select the top 5 companies with the highest market capitalization
top_5_companies = sorted_data.head(5)
print(top_5_companies.value_counts())
# Plot the market capitalization of the top 5 companies
plt.figure(figsize=(10, 6))
plt.bar(top_5_companies['Name'], top_5_companies['Mar Cap - Crore'])
plt.title('Top 5 Companies with Highest Market Capitalization')
plt.xlabel('Company')
plt.ylabel('Market Capitalization (Crore)')
plt.xticks(rotation=45)
plt.show()

# Sort the dataset by market capitalization in ascending order
sorted_data = df.sort_values('Mar Cap - Crore')
# Select the bottom 5 companies with the lowest market capitalization
bottom_5_companies = sorted_data.head(5)
print(bottom_5_companies.value_counts())
# Plot the market capitalization of the bottom 5 companies
plt.figure(figsize=(10, 6))
plt.bar(bottom_5_companies['Name'], bottom_5_companies['Mar Cap - Crore'])
plt.title('Bottom 5 Companies with Lowest Market Capitalization')
plt.xlabel('Company')
plt.ylabel('Market Capitalization (Crore)')
plt.xticks(rotation=45)
plt.show()

# Sort the dataset by sales in descending order
sorted_data = df.sort_values('Sales Qtr - Crore', ascending=False)
# Select the top 5 companies with the highest sales
top_5_companies_sales = sorted_data.head(5)
print(top_5_companies_sales.value_counts())
# Plot the sales of the top 5 companies
plt.figure(figsize=(10, 6))
plt.bar(top_5_companies_sales['Name'], top_5_companies_sales['Sales Qtr -
plt.title('Top 5 Companies with Highest Sales')
plt.xlabel('Company')
plt.ylabel('Sales (Crore)')
plt.xticks(rotation=45)
plt.show()

# Sort the dataset by sales in ascending order
sorted_data = df.sort_values('Sales Qtr - Crore')
# Select the bottom 5 companies with the highest sales
bottom_5_companies_sales = sorted_data.tail(5)
print(bottom_5_companies_sales.value_counts())
# Plot the sales of the bottom 5 companies
plt.figure(figsize=(10, 6))
plt.bar(bottom_5_companies_sales['Name'], bottom_5_companies_sales['Sales
plt.title('Bottom 5 Companies with Lowest Sales')
plt.xlabel('Company')
plt.ylabel('Sales (Crore)')
plt.xticks(rotation=45)
plt.show()

# Sort the dataset by profit margin in descending order
sorted_data = df.sort_values('Profit Margin', ascending=False)
# Select the top 5 companies with the highest profit margin
top_5_companies_pm = sorted_data.head(5)
print(top_5_companies_pm.value_counts())
# Plot the profit margin of the top 5 companies
plt.figure(figsize=(10, 6))
plt.bar(top_5_companies_pm['Name'], top_5_companies_pm['Profit Margin'])
plt.title('Top 5 Companies with Highest Profit Margin')
plt.xlabel('Company')
plt.ylabel('Profit Margin')
plt.xticks(rotation=45)
plt.show()

# Sort the dataset by profit margin in ascending order
sorted_data = df.sort_values('Profit Margin')
# Select the bottom 5 companies with the lowest profit margin
bottom_5_companies_pm = sorted_data.head(5)
print(bottom_5_companies_pm.value_counts())
# Plot the profit margin of the bottom 5 companies
plt.figure(figsize=(10, 6))
plt.bar(bottom_5_companies_pm['Name'], bottom_5_companies_pm['Profit Margi
plt.title('Bottom 5 Companies with Lowest Profit Margin')
plt.xlabel('Company')
plt.ylabel('Profit Margin')
plt.xticks(rotation=45)
plt.show()

# Sort the dataset by profit margin in descending order
sorted_data_MS = df.sort_values('Market_Share', ascending=False)
# Select the top 5 companies with the highest profit margin
top_5_companies_MS = sorted_data_MS.head(5)
print(top_5_companies_MS.value_counts())
# Plot the profit margin of the top 5 companies
plt.figure(figsize=(10, 6))
plt.bar(top_5_companies_MS['Name'], top_5_companies_MS['Market_Share'])
plt.title('Top 5 Companies with Highest Market_Share')
plt.xlabel('Company')
plt.ylabel('Market_Share')
plt.xticks(rotation=45)
plt.show()
