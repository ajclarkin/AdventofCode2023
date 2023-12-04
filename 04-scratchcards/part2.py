import re

lines = [x for x in open('input.txt').read().split('\n')]
input = list()
multiples = dict()


# First go through each input row and make a set from each scratch card
# Use the same loop to initialise multiples which will count how many of each card we have
for c, l in enumerate(lines):
    row = list()
    numbers = re.findall(r'\d+', l)
    # Values for example.txt
    # row.append({int(n) for n in numbers[-8:]})
    # row.append({int(n) for n in numbers[1:6]})

    row.append({int(n) for n in numbers[-25:]})
    row.append({int(n) for n in numbers[1:11]})
    input.append(row)

    multiples[c] = 1


# Now increment the multiples count for each of the matches
for rownum, i in enumerate(input):
    matches = len(i[0].intersection(i[1]))
    
    for j in range(multiples[rownum]):
        if matches > 0:
            for m in range(1, matches+1):
                multiples[rownum+m] += 1


total = sum(multiples.values())
print(f'The final total is {total}')
