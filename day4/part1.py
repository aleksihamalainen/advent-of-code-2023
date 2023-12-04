with open('input.txt') as f:
    input = f.read().splitlines()

card_points = []

for card in input:
    winning_numbers = card.split('|')[0].split(':')[1].split()
    my_numbers = card.split('|')[1].split()
    winning_numbers = [int(num) for num in winning_numbers]
    my_numbers = [int(num) for num in my_numbers]
    my_winning_numbers = list(set(winning_numbers).intersection(my_numbers))
    n = len(my_winning_numbers)
    points = 2 ** (n - 1) if n else 0
    card_points.append(points)

print(sum(card_points))