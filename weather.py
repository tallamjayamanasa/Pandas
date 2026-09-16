import pandas as pd
df=pd.read_csv('Weather.csv')
print(df)
print("Average Temperature:")
print(df["Temperature"].mean())


print("\nHottest City:")
print(df.loc[df["Temperature"].idxmax()])


print("\nColdest City:")
print(df.loc[df["Temperature"].idxmin()])


print("\nCities above 7°C:")
print(df[df["Temperature"] > 7])


print("\nSorted by Rainfall:")
print(df.sort_values("Rainfall", ascending=False))