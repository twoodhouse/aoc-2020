import pandas as pd

df = pd.read_csv('data/2.ssv', names=['range', 'letter', 'password'], delimiter=r"\s+")
df['letter'] = df['letter'].map(lambda x: x.strip(':'))
df['range_min'] = df['range'].map(lambda x: int(x.split('-')[0]))
df['range_max'] = df['range'].map(lambda x: int(x.split('-')[1]))
df['count'] = df.apply(lambda row: row['password'].count(row['letter']), axis=1)
df['valid'] = df.apply(lambda row: row['range_min'] <= row['count'] <= row['range_max'], axis=1)
print(df['valid'].sum())
