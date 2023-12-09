with open('input.txt') as f:
    input = f.read().splitlines()

def has_non_zeros(diffs):
    return any(x != 0 for x in diffs)

def calculate_diffs(history):
    return [history[i + 1] - history[i] for i in range(len(history) - 1)]

extrapolated_values = []

for row in input:
    history = list(map(int, row.split()))
    layers = [history]
    while has_non_zeros(layers[-1]):
        diffs = calculate_diffs(layers[-1])
        layers.append(diffs)
    layers[-1].append(0)
    for i in range(len(layers) - 2, -1, -1):
        layers[i].append(layers[i][-1] + layers[i + 1][-1])
    extrapolated_values.append(layers[0][-1])

print(sum(extrapolated_values))