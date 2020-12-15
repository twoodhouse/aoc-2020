from copy import deepcopy
import pandas as pd

with open("real.txt") as fp:
    table = []
    for line in fp:
        lst = []
        for c in line:
            if c is not '\n':
                lst.append(c)
        table.append(lst)
# # Part 1
# changed=True
# while changed:
#     new_table = deepcopy(table)
#     changed = False
#     for row_i, row in enumerate(table):
#         for col_i, val in enumerate(row):
#             # Count those around
#             count = 0
#             for i in range(3):
#                 for j in range(3):
#                     if 0 <= row_i-1+i < len(table) and 0 <= col_i-1+j < len(row) and table[row_i-1+i][col_i-1+j] == '#' and not (i == 1 and j == 1):
#                         count += 1
#             # print('{}, {}, = {}'.format(row_i, col_i, count))
#             if val == 'L':
#                 if count == 0:
#                     new_table[row_i][col_i] = '#'
#                     changed = True
#             elif val == '#':
#                 if count >= 4:
#                     new_table[row_i][col_i] = 'L'
#                     changed = True
#     # print(new_table)
#     table = new_table

# Part 2
changed = True
while changed:
    new_table = deepcopy(table)
    changed = False
    for row_i, row in enumerate(table):
        for col_i, val in enumerate(row):
            # Count those around
            count = 0
            for i in range(3):
                for j in range(3):
                    if not (i == 1 and j == 1):
                        done_looking = False
                        mod_i = i - 1
                        mod_j = j - 1
                        while not done_looking:
                            if not (0 <= row_i+mod_i < len(table) and 0 <= col_i+mod_j < len(row)):
                                done_looking = True
                            elif table[row_i+mod_i][col_i+mod_j] == '#':
                                count += 1
                                # print(str(i) + ', ' + str(j))
                                done_looking = True
                            elif table[row_i+mod_i][col_i+mod_j] == 'L':
                                done_looking = True
                            else:
                                mod_i = mod_i + (i-1)
                                mod_j = mod_j + (j-1)


            # print('{}, {}, = {}'.format(row_i, col_i, count))
            if val == 'L':
                if count == 0:
                    new_table[row_i][col_i] = '#'
                    changed = True
            elif val == '#':
                if count >= 5:
                    new_table[row_i][col_i] = 'L'
                    changed = True
    # print(pd.DataFrame(new_table))
    table = new_table

count_occupied = 0

for row in table:
    for val in row:
        if val == '#':
            count_occupied += 1

print(count_occupied)

