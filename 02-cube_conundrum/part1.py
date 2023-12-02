'''
    We want to add up all the games where limit is not exceeded.
    Start with max possible total and remove the games where limit exceeded.
'''

import re

input = [x for x in open('input.txt').read().split('\n')]

limits = {'red': 12,
          'green': 13,
          'blue': 14
          }

total = 101*50

for i in input:
    pairs = re.findall('\d+ \w+', i)
    
    for p in pairs:
        num, colour = p.split(' ')
        if int(num) > limits[colour]:
            game = re.findall('(\d+)\:', i)[0]
            total -= int(game)
            break

print(f'The final total is {total}')