import pandas as pd
df=pd.read_csv('IPL.csv')
print(df)

print("Highest Runs:")
print(df.loc[df["Runs"].idxmax()])

print("\nTop 5 Players:")
print(df.nlargest(5, "Runs"))

print("\nTeam-wise Average:")
print(df.groupby("Team")["Runs"].mean())

print("\nHighest Strike Rate:")
print(df.loc[df["Strike Rate"].idxmax()])

print("\nPlayers Sorted by Runs:")
print(df.sort_values("Runs", ascending=False))