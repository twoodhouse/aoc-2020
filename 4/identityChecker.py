import pandas as pd
import re

def add_to_dict(d, keys):
    for key in keys.split(' '):
        d[key.split(':')[0]] = key.split(':')[1]

def validate_height(height):
    if height[-2:] == 'in':
        return height if 59 <= int(height[:-2]) <= 76 else None
    elif height[-2:] == 'cm':
        return height if 150 <= int(height[:-2]) <= 193 else None
    else:
        return None




identities = []
with open("3.identifications") as fp:
    cnt = 1
    identity = {}
    line = None
    while line or cnt == 1:
        line = fp.readline()
        if line.strip() == "":
            identities.append(identity)
            identity = {}
        else:
            add_to_dict(identity, line.strip())
        cnt += 1

df = pd.DataFrame(identities)
df = df[['byr', 'iyr', 'hgt', 'eyr', 'ecl', 'pid', 'hcl']]
df = df.dropna()

df['byr'] = df['byr'].map(lambda x: x if 1920 <= int(x) <= 2002 else None)
df['iyr'] = df['iyr'].map(lambda x: x if 2010 <= int(x) <= 2020 else None)
df['eyr'] = df['eyr'].map(lambda x: x if 2020 <= int(x) <= 2030 else None)
df['hgt'] = df['hgt'].map(validate_height)
df['hcl'] = df['hcl'].map(lambda x: x if x[0] == '#' and re.search(r"^[a-f0-9]{6}$", x[1:]) else None)
df['ecl'] = df['ecl'].map(lambda x: x if x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else None)
df['pid'] = df['pid'].map(lambda x: x if re.search(r"^[0-9]{9}$", x) else None)

df = df.dropna()
print(df)