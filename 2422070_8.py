import pandas as pd

df = pd.read_csv('winequality-red.csv')
filtered_df = df[df["quality"] >= 6]
sorted_df = filtered_df.sort_values(by='quality', ascending=False)

print(sorted_df)