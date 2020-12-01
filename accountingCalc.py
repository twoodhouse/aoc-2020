import pandas as pd

df = pd.read_csv('data/1.csv', names=['val'])
print(df)
for index, row in df.iterrows():
    for index2, row2 in df.iterrows():
        if index != index2:
            if row['val'] + row2['val'] < 2020:
                for index3, row3 in df.iterrows():
                    if row['val'] + row2['val'] + row3['val'] == 2020:
                        print(row['val'] * row2['val'] * row3['val'])