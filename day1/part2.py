import re

with open('input.txt') as f:
    input = f.read().splitlines()

calibration_values = []

digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

for i in input:
    matches = re.findall(pattern, i)
    first = matches[0]
    last = matches[-1]
    digit_first = digit_map.get(first, first)
    digit_last = digit_map.get(last, last)
    calibration_values.append(int(digit_first + digit_last))

print(sum(calibration_values))