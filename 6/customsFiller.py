groups = []
with open("6.sv") as fp:
    cnt = 1
    group = []
    line = None
    while line or cnt == 1:
        line = fp.readline()
        if line.strip() == "":
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
        cnt += 1

# print(groups)

# # Part 1
# counts = []
# qs = set()
# for group in groups:
#     for person in group:
#         for letter in person:
#             qs.add(letter)
#     counts.append(len(qs))
#     qs = set()
#
# print(counts)
# print(sum(counts))

# Part 2
counts = []
for group in groups:
    sets = []
    for person in group:
        st = set()
        for letter in person:
            st.add(letter)
        sets.append(st)
    res = sets[0].intersection(*sets)
    counts.append(len(res))

print(counts)
print(sum(counts))