import pandas as pd

def valList_to_num(lst):
    out = 0
    for bit in lst:
        out = (out << 1) | bit
    return out

df = pd.read_csv('tickets.sv', names=['ticket'])
df['row'] = df['ticket'].map(lambda x: valList_to_num(map(lambda x: False if x == 'F' else True, list(x[:7]))))
df['column'] = df['ticket'].map(lambda x: valList_to_num(map(lambda x: False if x == 'L' else True, list(x[-3:]))))
df['seat_id'] = df.apply(lambda row: row['row']*8 + row['column'], axis=1)
print(df)
print(df['seat_id'].max())

#Part 2
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df.groupby('row').count()) # Visually, answer is row 81
print(df[df['row']==81]) # Visually, column is 3
print(81 * 8 + 3)