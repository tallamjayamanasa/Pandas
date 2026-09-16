import pandas as pd

df = pd.read_csv("Bank.csv")
print(df)
print(df.columns)
print("Highest Balance:")
print(df.loc[df["Balance "].idxmax()])
print("\nLowest Balance:")
print(df.loc[df["Balance "].idxmin()])
print("\nCity-wise Customers:")
print(df.groupby("City")["Customer_ID"].count())
print("\nTotal Balance:")
print(df["Balance"].sum())

