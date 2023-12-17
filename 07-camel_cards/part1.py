from collections import Counter


input = [x for x in open('input.txt').read().split()]
card_values = dict()
card_ranks = [[],[],[],[],[],[],[]]
precedence = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
total = 0

cards = input[::2]
bids = input[1::2]

for c, b in zip(cards, bids):
    card_values[c] = int(b) 


for c in cards:
    repcount = Counter(Counter(c).values())
    # Inner counter returns this: Counter({'3': 2, '2': 1, 'T': 1, 'K': 1})
    # Outer counter returns this: 32T3K Counter({1: 3, 2: 1})

    if repcount.get(5):
        card_ranks[0].append(c)
    elif repcount.get(4):
        card_ranks[1].append(c)
    elif repcount.get(3) and repcount.get(2):
        card_ranks[2].append(c)
    elif repcount.get(3) and repcount.get(1):
        card_ranks[3].append(c)
    elif repcount.get(2) and repcount[2] == 2:
        card_ranks[4].append(c)
    elif repcount.get(2) and repcount[2] == 1:
        card_ranks[5].append(c)
    elif repcount.get(1) and repcount[1] == 5:
        card_ranks[6].append(c)



# Bubblesort


    
for rank in card_ranks:
    changed = True
    while changed:
        print(f'rank: {rank}')
        changed = False
        for hand in range(len(rank)-1):
            print(f'Consider hand {rank[hand]}')
            for i in range(5):
                if precedence.index(rank[hand][i]) > precedence.index(rank[hand+1][i]):
                    print(f'swap {rank[hand]} {rank[hand+1]} (char {i})')
                    rank[hand], rank[hand+1] = rank[hand+1], rank[hand]
                    changed = True
                    break
                elif precedence.index(rank[hand][i]) < precedence.index(rank[hand+1][i]):
                    break


rankno = len(cards)

for rank in card_ranks:
    for hand in rank:
        total += rankno * card_values[hand]
        rankno -= 1

print(total)