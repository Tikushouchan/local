import pandas as pd

df_1 = pd.read_csv('items - items.csv')
df_2 = pd.read_csv('orders - orders.csv')
df_3 = pd.read_csv('users - users.csv')
df_new_1 = pd.merge(df_1, df_2, on='item_id')
df_new_2 = pd.merge(df_new_1, df_3, on='user_id')
#print(df_new_2)

df_new_2['平均購入金額'] = df_new_2['item_price'] * df_new_2['order_num'].min()
print(df_new_2[['user_id', '平均購入金額']])
print(df_new_2['平均購入金額'].max())