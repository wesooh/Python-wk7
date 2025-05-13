# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the dataset
try:
    data = pd.read_csv("sales_data.csv")
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print("❌ sales_data.csv not found. Please check the file path.")

# Step 3: Display the first few rows
print("\n📊 First 5 rows:")
print(data.head())

# Step 4: Check data types and missing values
print("\n🔍 Data Types:")
print(data.dtypes)

print("\n❓ Missing Values:")
print(data.isnull().sum())

# Step 5: Basic Data Analysis
print("\n📈 Basic Statistics:")
print(data.describe())

print("\n📦 Unique Product Categories:")
print(data['Category'].unique())

print("\n💰 Average Revenue per Category:")
print(data.groupby('Category')['Revenue'].mean())

# Step 6: Data Visualization

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# 1. Line Chart: Revenue Over Time
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Revenue'], color='blue', marker='o')
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar Chart: Total Revenue by Category
category_revenue = data.groupby('Category')['Revenue'].sum()
plt.figure(figsize=(8, 5))
category_revenue.plot(kind='bar', color='green')
plt.title('Total Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of Units Sold
plt.figure(figsize=(8, 5))
plt.hist(data['Units_Sold'], bins=10, color='purple', edgecolor='black')
plt.title('Distribution of Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Units Sold vs. Revenue
plt.figure(figsize=(8, 5))
plt.scatter(data['Units_Sold'], data['Revenue'], color='red')
plt.title('Units Sold vs. Revenue')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()


# === Observations ===
print("\n--- Observations ---")
print("""
1. Electronics category has higher average revenue compared to Clothing.
2. Most products are sold between 10 to 40 units.
3. Revenue seems to grow over time.
4. Units Sold and Revenue have a positive relationship.
""")