import pandas as pd

df = pd.read_csv('items - items.csv')
df_1 = df[df['item_id'] == 101]

