from collections import Counter

# Note the changed order of precedence - J has moved to the bottom

input = [x for x in open('input.txt').read().split()]
card_values = dict()
card_ranks = [[],[],[],[],[],[],[]]
precedence = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
total = 0

cards = input[::2]
bids = input[1::2]

for c, b in zip(cards, bids):
    card_values[c] = int(b) 


for c in cards:
    cardcount = Counter(c)
    repcount = Counter(Counter(c).values())
    # Inner counter returns this: Counter({'3': 2, '2': 1, 'T': 1, 'K': 1})
    # Outer counter returns this: 32T3K Counter({1: 3, 2: 1})

    if 'J' in c:
        j_count = cardcount['J']

    # This is a bit untidy
    # Same as part 1 if there are no J present
    # If there is a J then it acts to create the highest rank possible
    #   So, in 4 of a kind any J will make it a 5 (JJJJ + X OR XXXX + J)
    #   In full house any J makes it a 5: (JJJ + XX OR XXX + JJ)
    # So for each we look to see what effect a J could have and upgrade the rank if required
        
    if repcount.get(5):
        card_ranks[0].append(c)
    elif repcount.get(4):
        card_ranks[0].append(c) if 'J' in c else card_ranks[1].append(c)
    elif repcount.get(3) and repcount.get(2):
        card_ranks[0].append(c) if 'J' in c else card_ranks[2].append(c)
    elif repcount.get(3) and repcount.get(1):
        card_ranks[1].append(c) if 'J' in c else card_ranks[3].append(c)
    elif repcount.get(2) and repcount[2] == 2:
        if 'J' in c and j_count == 1:
            card_ranks[2].append(c)
        elif 'J' in c and j_count == 2:
            card_ranks[1].append(c)
        else:
            card_ranks[4].append(c)
    elif repcount.get(2) and repcount[2] == 1:
        card_ranks[3].append(c) if 'J' in c else card_ranks[5].append(c)
    elif repcount.get(1) and repcount[1] == 5:
        card_ranks[5].append(c) if 'J' in c else card_ranks[6].append(c)



# Bubblesort

    
for rank in card_ranks:
    changed = True
    while changed:
        changed = False
        for hand in range(len(rank)-1):
            for i in range(5):
                if precedence.index(rank[hand][i]) > precedence.index(rank[hand+1][i]):
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


print(f'The total value is {total}')

