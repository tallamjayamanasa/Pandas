import pandas as pd
df=pd.read_csv('ecommerce.csv')

# 1. Most Expensive Product
print("Most Expensive Product:")
print(df.loc[df["Price"].idxmax()])

# 2. Cheapest Product
print("\nCheapest Product:")
print(df.loc[df["Price"].idxmin()])

# 3. Average Rating
print("\nAverage Rating:")
print(df["Rating"].mean())

# 4. Category-wise Products
print("\nCategory-wise Products:")
print(df.groupby("Category")["Product"].count())

# 5. Total Inventory Value
df["Inventory_Value"] = df["Price"] * df["Quantity"]

print("\nTotal Inventory Value:")
print(df["Inventory_Value"].sum())