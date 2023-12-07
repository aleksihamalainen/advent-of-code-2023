from collections import defaultdict
from functools import cmp_to_key

with open('input.txt') as f:
    input = f.read().splitlines()

labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_type(hand):
    counts = defaultdict(int)
    jokers = 0
    for char in hand:
        if char == 'J':
            jokers += 1
        else:
            counts[char] += 1
    sorted_counts = sorted(counts.values(), reverse=True)
    if jokers == 5 or sorted_counts[0] + jokers == 5:
        return 7
    if sorted_counts[0] + jokers == 4:
        return 6
    if sorted_counts[0] + jokers == 3:
        remaining_jokers = jokers - (3 - sorted_counts[0])
        if sorted_counts[1] + remaining_jokers == 2:
            return 5
        return 4
    if sorted_counts[0] + jokers == 2:
        remaining_jokers = jokers - (2 - sorted_counts[0])
        if sorted_counts[1] + remaining_jokers == 2:
            return 3
        return 2
    return 1

def compare(a, b):
    a_type = get_type(a)
    b_type = get_type(b)
    if a_type == b_type:
        if a == b:
            return 0
        for i in range(5):
            if labels.index(a[i]) < labels.index(b[i]):
                return 1
            if labels.index(a[i]) > labels.index(b[i]):
                return -1
    if a_type > b_type:
        return 1
    return -1
    
hand_bid_pairs = []

for line in input:
    hand, bid = line.split()
    hand_bid_pairs.append((hand, int(bid)))

hand_bid_pairs_sorted = sorted(hand_bid_pairs, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))

total_winnings = 0

for i in range(len(hand_bid_pairs_sorted)):
    total_winnings += hand_bid_pairs_sorted[i][1] * (i + 1)

print(total_winnings)