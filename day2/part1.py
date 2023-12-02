with open('input.txt') as f:
    inputs = f.read().splitlines()

bag_content = {
    'red': 12,
    'green': 13,
    'blue': 14
}

possible_games = []

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
    has_negatives = False
    for dict in dict_list:
        cube_diff = {k: bag_content[k] - dict.get(k, 0) for k in bag_content}
        has_negatives = any(value < 0 for value in cube_diff.values())
        if has_negatives:
            break
    if not has_negatives:
        possible_games.append(i + 1)

print(sum(possible_games))