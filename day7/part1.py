from collections import defaultdict
from functools import cmp_to_key

with open('input.txt') as f:
    input = f.read().splitlines()

labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def get_type(hand):
    counts = defaultdict(int)
    for char in hand:
        counts[char] += 1
    sorted_counts = sorted(counts.values(), reverse=True)
    if sorted_counts == [5]:
        return 7
    if sorted_counts == [4, 1]:
        return 6
    if sorted_counts == [3, 2]:
        return 5
    if sorted_counts == [3, 1, 1]:
        return 4
    if sorted_counts == [2, 2, 1]:
        return 3
    if sorted_counts == [2, 1, 1, 1]:
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