import pandas as pd
data = pd.read_csv("sales_data.csv")
print(data.head())

print("\nData Types:")
print(data.dtypes)

print("\nMissing Values:")
print(data.isnull().sum())
