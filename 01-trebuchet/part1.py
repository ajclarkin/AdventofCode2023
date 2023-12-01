import re

input = [x for x in open('input.txt').read().split('\n')]
total = 0

digitnames = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
              'six': 6, 'seven': 7, 'eight': 8, 'nine':9}


def convert_int(numstring):
    if len(numstring) == 1:
        return(int(numstring))
    else:
        return digitnames[numstring]


for i in input:
    # if you don't include the ?= then overlapping numbers won't be found, eg twone will only return two
    numbers = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', i)

    if len(numbers) > 1:
        total = total + convert_int(numbers[0])*10 + convert_int(numbers[-1])
    elif len(numbers) == 1:
        total = total + convert_int(numbers[0])*10 + convert_int(numbers[0])
    else:
        pass


print(f'The final total is: {total}')