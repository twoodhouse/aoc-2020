from copy import deepcopy
import pandas as pd
import math

start = None
commands = []
with open("real.txt") as fp:
    for index, line in enumerate(fp):
        if line[:4] == 'mask':
            commands.append(('mask', line.split(' ')[-1].strip()))
        else:
            commands.append(('mem', (int(line.split('[')[1].split(']')[0]), int(line.split(' ')[-1].strip()))))

print(commands)


def num_to_bin(num, digits=36):
    return format(num, '#0' + str(digits + 2) + 'b')[2:]


def bin_to_num(bin):
    return int(bin, 2)


# #Part 1
# def mask_transform(val, mask):
#     b = list(num_to_bin(val))
#     print(b)
#     print(mask)
#     for i, e in enumerate(mask):
#         if e != 'X':
#             b[i] = str(e)
#     return bin_to_num(''.join(b))
#
# memory = {}
# mask = None
# for key, val in commands:
#     if key == 'mask':
#         mask = val
#     elif key == 'mem':
#         memory[val[0]] = mask_transform(val[1], mask)
#
# print(sum(memory.values()))

#Part 2
def mask_transform(address, value, mask, memory):
    b = list(num_to_bin(address))
    x_locations = []
    for i, e in enumerate(mask):
        if e == '0':
            pass
        elif e == '1':
            b[i] = str(1)
        elif e == 'X':
            b[i] = str(0)
            x_locations.append(35-i)
    print(mask)
    print(b)
    base = bin_to_num(''.join(b))
    x_vals = list(map(lambda x: 2**x, x_locations))

    print(x_locations)
    locations = []
    for i in range(2 ** len(x_vals)):
        st = num_to_bin(i, len(x_vals))
        sum = base
        for j, e in enumerate(list(st)):
            if e == '1':
                sum += x_vals[j]
        locations.append(sum)

    print(locations)

    for location in locations:
        memory[location] = value


memory = {}
mask = None
for key, val in commands:
    if key == 'mask':
        mask = val
    elif key == 'mem':
        mask_transform(val[0], val[1], mask, memory)

print(memory)
print(sum(memory.values()))