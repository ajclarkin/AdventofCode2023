from math import sqrt, floor
import re

lines = [x for x in open('input.txt').read().split('\n')]
input = list()
for l in lines:
    input.append(''.join(re.findall('\d', l)))
   

values = list()
total = 1

duration = int(input[0])
distance = int(input[1])


r1 = (duration - sqrt((duration * duration) - (4 * 1 * distance))) / (2)
r2 = (duration + sqrt((duration * duration) - (4 * 1 * distance))) / (2)
print(r1, r2, (floor(r2) - floor(r1)))