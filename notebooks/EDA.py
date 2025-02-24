import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Current Working Directory:", os.getcwd())

# Load CSV files using paths relative to the main directory
sales_data = pd.read_csv('data/sales_data_set.csv')
stores_data = pd.read_csv('data/stores_data_set.csv')
features_data = pd.read_csv('data/features_data_set.csv')

print(sales_data.head())
print(sales_data.describe())

# Convert the 'Date' column to datetime using the correct format (day first)
sales_data['Date'] = pd.to_datetime(sales_data['Date'], format='%d/%m/%Y')
# Alternatively:
# sales_data['Date'] = pd.to_datetime(sales_data['Date'], dayfirst=True)

plt.figure(figsize=(10, 5))
plt.plot(sales_data['Date'], sales_data['Weekly_Sales'])
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.title('Sales Over Time')
plt.gcf().autofmt_xdate()
plt.show()