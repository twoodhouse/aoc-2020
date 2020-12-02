import pandas as pd

df = pd.read_csv('2.ssv', names=['range', 'letter', 'password'], delimiter=r"\s+")
df['letter'] = df['letter'].map(lambda x: x.strip(':'))
df['req_a'] = df['range'].map(lambda x: int(x.split('-')[0]))
df['req_b'] = df['range'].map(lambda x: int(x.split('-')[1]))
df['req_a_match'] = df.apply(lambda row: row['password'][row['req_a']-1] == row['letter'], axis=1)
df['req_b_match'] = df.apply(lambda row: len(row['password'])>=row['req_b'] and row['password'][row['req_b']-1] == row['letter'], axis=1)

df['valid'] = df.apply(lambda row: row['req_a_match'] != row['req_b_match'], axis=1)
print(df)
print(df['valid'].sum())
