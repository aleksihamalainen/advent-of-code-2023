with open('input.txt') as f:
    input = f.read().splitlines()

copies = {i: 1 for i in range(len(input))}

for i, card in enumerate(input):
    winning_numbers = card.split('|')[0].split(':')[1].split()
    my_numbers = card.split('|')[1].split()
    winning_numbers = [int(num) for num in winning_numbers]
    my_numbers = [int(num) for num in my_numbers]
    my_winning_numbers = list(set(winning_numbers).intersection(my_numbers))
    n = len(my_winning_numbers)
    for j in range(i+1, i+n+1):
        copies[j] += copies[i]

print(sum(copies.values()))