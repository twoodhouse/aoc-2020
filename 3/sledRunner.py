import pandas as pd

df = pd.read_csv('3.sv', names=['hill'])


def count_hits(df, movement, only_mod=1):
    hits = 0
    counter = 1
    for index, row in df.iterrows():
        if index != 0 and index % only_mod == 0:
            if row['hill'][(counter*movement)%len(row['hill'])] == '#':
                hits += 1
            counter += 1
    return hits

# print(count_hits(df, 3))
print(count_hits(df, 1) * count_hits(df, 3) * count_hits(df, 5) * count_hits(df, 7) * count_hits(df, 1, only_mod=2))