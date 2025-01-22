import pandas as pd
df = pd.read_csv('winequality-red.csv')
quality_mean = df.groupby('quality').mean()
print(quality_mean)