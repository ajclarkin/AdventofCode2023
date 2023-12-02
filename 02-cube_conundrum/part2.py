'''
    For each game find the minimum number of each colour required.
    That corresponds to the highest number drawn of each colour in each game.
'''

import re

input = [x for x in open('input.txt').read().split('\n')]

total = 0

for i in input:
    reds = [int(x) for x in re.findall('(\d+) red', i)]
    greens = [int(x) for x in re.findall('(\d+) green', i)]
    blues = [int(x) for x in re.findall('(\d+) blue', i)]

    total += max(reds) * max(greens) * max(blues)


print(f'The final total is {total}')