import pandas as pd

df= pd.read_csv('chpt1.csv')

# print(df['வார்த்தைகள்'].nunique())

# print(df.groupby(['வார்த்தைகள்']).size().reset_index(name='count'))

df = df.pivot_table(columns=['வார்த்தைகள்'], aggfunc='size')
print(df)

df.to_csv('data.csv', encoding='utf-8')

