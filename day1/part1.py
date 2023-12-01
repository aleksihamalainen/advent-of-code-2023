import re

with open('input.txt') as f:
    input = f.read().splitlines()

calibration_values = []

for i in input:
    matches = [x for x in re.findall(r'\d', i)]
    first = matches[0]
    last = matches[-1]
    calibration_values.append(int(first + last))

print(sum(calibration_values))