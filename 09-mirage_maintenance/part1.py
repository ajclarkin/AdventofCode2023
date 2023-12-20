from collections import Counter

input = [[int(char) for char in row.split()] for row in open('input.txt').read().split('\n')]


row = list()
row.append(input[2])
total = 0

for i in input:
    row = list()
    row.append(i)

    while Counter(row[-1])[0] != len(row[-1]):
        l = list()
        for i in range(len(row[-1])-1):
            l.append(row[-1][i+1] - row[-1][i])

        row.append(l)

    #print(row)
    row[-1].append(0)

    for j in range(len(row)-2, -1, -1):
        row[j].append(row[j][-1] + row[j+1][-1])

    #print(row)

    total += row[0][-1]


print(f'The final total is {total}')
