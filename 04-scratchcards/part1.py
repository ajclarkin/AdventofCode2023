import re

lines = [x for x in open('input.txt').read().split('\n')]
input = list()
total = 0


for l in lines:
    row = list()
    numbers = re.findall(r'\d+', l)
    # These are the values for example.txt
    # row.append({int(n) for n in numbers[-8:]})
    # row.append({int(n) for n in numbers[1:6]})

    row.append({int(n) for n in numbers[-25:]})
    row.append({int(n) for n in numbers[1:11]})
    input.append(row)


for i in input:
    matches = len(i[0].intersection(i[1]))

    if matches > 0:
        total += pow(2, matches-1)

print(f'The final total is {total}')