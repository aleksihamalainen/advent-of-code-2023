with open('input.txt') as f:
    grid = f.read().splitlines()

rows = len(grid)
cols = len(grid[0])

vals = [[[] for _ in range(cols)] for _ in range(rows)]

sum = 0

def add_nums(i, j, num):
    if 0 <= i < rows and 0 <= j < cols:
        if grid[i][j] == '*':
            vals[i][j].append(num)

for i, row in enumerate(grid):
    start = 0
    j = 0
    while j < cols:
        start = j
        num = ''
        while j < cols and row[j].isdigit():
            num += row[j]
            j += 1
        if num == '':
            j += 1
            continue
        num = int(num)
        add_nums(i, start-1, num)
        add_nums(i, j, num)
        for k in range(start-1, j+1):
            add_nums(i-1, k, num)
            add_nums(i+1, k, num)

for i in range(rows):
    for j in range(cols):
        values = vals[i][j]
        if grid[i][j] == '*' and len(values) ==  2:
            sum += values[0] * values[1]

print(sum)