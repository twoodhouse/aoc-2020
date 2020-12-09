import pandas as pd

df = pd.read_csv('8.txt', names=['cmd', 'val'], delimiter=" ")

solution_found = False
to_swap = 0
while solution_found == False:
    acc = 0
    position = 0
    completed_rows = set()
    swap_counter = 0
    while position not in completed_rows and position < len(df.index):
        completed_rows.add(position)
        row = df.iloc[position]

        if to_swap == swap_counter and row.cmd != 'acc':
            if row.cmd == 'nop':
                row.cmd = 'jmp'
            else:
                row.cmd = 'nop'

        if row.cmd == 'acc':
            acc += row.val
            position += 1
        elif row.cmd == 'jmp':
            position += row.val
            swap_counter += 1
        elif row.cmd == 'nop':
            position += 1
            swap_counter += 1
        # print(position)

    if position == len(df.index):
        solution_found = True
        print(to_swap)
    to_swap += 1
print(acc)