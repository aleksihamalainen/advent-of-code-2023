with open('input.txt') as f:
    inputs = f.read().splitlines()

bag_content = {
    'red': 12,
    'green': 13,
    'blue': 14
}

powers = []

for i, input in enumerate(inputs):
    parsed = input.split(': ')[1:][0]
    sets = parsed.split('; ')
    pairs = [set.split(', ') for set in sets]
    dict_list = []
    for pair in pairs:
        set_dict = {}
        for item in pair:
            number, color = item.split()
            set_dict[color] = int(number)
        dict_list.append(set_dict)
    max_dict = {}
    for key in bag_content.keys():
        max_dict[key] = max(dict.get(key, 0) for dict in dict_list)
    power = 1
    for key in bag_content.keys():
        power *= max_dict[key]
    powers.append(power)

print(sum(powers))