import pandas as pd

df = pd.read_csv('9.txt', names=['v'], delimiter=" ")

# a = []
# for index, row in df.iterrows():
#     if index < 25:
#         a.append(row.v)
#     else:
#         #Verify
#         allowed = False
#         for i in a:
#             for j in a:
#                 if i + j == row.v and i != j:
#                     allowed = True
#         if not allowed:
#             # print(row.v)
#             pass
#         a.pop(0)
#         a.append(row.v)

# # Part 2
# key = 217430975
# df = df.reindex(index=df.index[::-1])
# for index, row in df.iterrows():
#     sum = 0
#     lst = []
#     k = index
#     while sum < key:
#         sum += df.iloc[k].v
#         lst.append(df.iloc[k].v)
#         k -= 1
#     if sum == key:
#         print(str(index) + ' ' + str(k+1) + str(lst))

x = [11693198, 12266770, 9703408, 13518723, 10026448, 13861085, 10368810, 12036398, 11431324, 11511108, 11570262, 12757245, 12470181, 13752180, 18805772, 15551150, 16106913]
print(min(x) + max(x))