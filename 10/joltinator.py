import pandas as pd

df = pd.read_csv('10.txt', names=['jolts'])
df = df.append({'jolts': 0}, ignore_index=True)
df = df.sort_values(by='jolts', ignore_index=True)

# print(df)

#Part 1
# prior = 0
# count_ones = 0
# count_threes = 0
# for index, row in df.iterrows():
#     if row.jolts - prior == 1:
#         count_ones += 1
#     elif row.jolts - prior == 3:
#         count_threes += 1
#     prior = row.jolts
#
# print(count_ones * (count_threes + 1))

#Part 2

combos = []
river = []
for index, row in df.iterrows():
    combos_sum = 0
    for river_index, plug in enumerate(river):
        if row.jolts - plug <= 3:
            combos_sum += combos[index - len(river) + river_index]
    if len(river) == 0:
        combos_sum = 1
    combos.append(combos_sum)
    # Prepare for next
    river.append(row.jolts)
    if len(river) > 3:
        river.pop(0)

print(combos[-1])