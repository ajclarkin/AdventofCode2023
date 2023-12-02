import re

input = [x for x in open('input.txt').read().split('\n')]
total = 0

for i in input:
    # Each of the variables is a list and will contain a string if digit present
    tens = re.findall(r'^\D*(\d)', i)
    units = re.findall(r'\S*(\d)\D*$', i)

    if (len(tens) > 0) & (len(units) > 0):
        total = total + int(tens[0])*10 + int(units[0])

print(f'The final total is: {total}')