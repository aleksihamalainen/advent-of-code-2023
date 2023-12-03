with open('input.txt') as f:
    grid = f.read().splitlines()

rows = len(grid)
cols = len(grid[0])

sum = 0

def is_symbol(i, j):
    if not (0 <= i < rows and 0 <= j < cols):
        return False
    return grid[i][j] != '.' and not grid[i][j].isdigit()

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
        if is_symbol(i, start-1) or is_symbol(i, j):
            sum += num
            continue
        for k in range(start-1, j+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                sum += num
                break

print(sum)