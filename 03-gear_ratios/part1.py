import re
input = [x for x in open('input.txt').read().split('\n')]
punctpos = set()
total = 0

# Make a set containing the (row, col) of each punctuation mark
for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        if not char.isdigit() and char != '.':
            punctpos.add((rownum, colnum))


# For each number identify the coordinates surrounding
# We need to add on the diagonals and make sure the new coordinate actually exists
# The check if any of them are in punctpos - if they are then this is a valid part
# NOTE - used re.finditer to avoid edge case

linewidth = range(len(input[0]))
for rownum, row in enumerate(input):
    for n in re.finditer(r'\d+', row):
        value = int(n.group())
        span = n.span()
        surrounds = list()

        # left
        if span[0]-1 in linewidth:
            surrounds.append((rownum, span[0]-1))
        # right
        if span[0]+1 in linewidth:
            surrounds.append((rownum, span[1]))
        # top
        surrounds.extend([(rownum-1, x) for x in range(span[0]-1, span[1]+1) if rownum-1 >=0 and x in linewidth])
        # bottom
        surrounds.extend([(rownum+1, x) for x in range(span[0]-1, span[1]+1) if rownum+1 < len(input) and x in linewidth])


        # Now check if any of the surround are a punctuation symbol. If they are then add to list.
        for s in surrounds:
            if s in punctpos:
                total += value
                break

print(f'The final total is {total}')