from copy import deepcopy
import pandas as pd
import math

start = None
buses = []
with open("real.txt") as fp:
    for index, line in enumerate(fp):
        if index == 0:
            start = int(line.strip())
        else:
            for c in line.strip().split(','):
                buses.append(c)
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

#Part 1
# buses = list(filter(lambda x: x != 'x', buses))
# found = False
# time = start
# while not found:
#     for bus in buses:
#         if time % int(bus) == 0:
#             print((time-start)*int(bus))
#             found = True
#     time += 1

##Part 2

first = 14173779
first_index = 0
recurrence = 17371741
found = False
start_time = first - first_index
time = start_time
while not found:
    if (time-start_time) % ((recurrence) * 100000) == 0:
        print(time)
    found = True
    for bus_index, bus in enumerate(buses):
        if bus != 'x':
            if (time + bus_index) % int(bus) == 0:
                pass
            else:
                found = False
                break
    if found:
        print(time)
        break
    time += recurrence
    # time += 14173782-1

# found = False
# time = 0
# # recurrenct, regular offset, single offset
# # buses = [(641, 13, 0), (661, 44, 0)]
# buses = [(423701, 0, 191646), (41, 3, 0)]
# # buses = [(59, 0), (31, 2)]
#
# while not found:
#     if time % 1000000 == 0:
#         print(time)
#     found = True
#     for bus, offset, initial_offset in buses:
#         if bus != 'x':
#             if (time + offset) % int(bus) - initial_offset == 0:
#                 pass
#             else:
#                 found = False
#                 break
#     if found:
#         print(time)
#         print(lcm(*[x[0] for x in buses]))
#     time += 1