# If You Give a Seed a Fertilizer
Ok, easy part 1, difficult part 2. This feels like a tought AoC this year, I'm surprised at part
2 so early on but again perhaps I'm missing something.

## Features
Really just text parsing and dictionary methods.


## Part 1
Pretty straightforward. I build a dictionary for each of the conversions with the range of the source
seed as a tuple for the key and the change to make as the value. Then it's just a case of iterating through
doing comparisons and adding the value if needed.

Here's some example code:


```python
ranges = {
    (1, 10): 5,
    (11, 20): 10, 
    (21, 30): 15
}

# Where test would be the seed values and we're going to check if they appear in the ranges dict.
test = [1,10,13,40]

keys = ranges.keys()
for t in test:
    for k in keys:
        if k[0] <= t <= k[1]:
            print(f'{t} is between {k[0]} and {k[1]}. New t = {t + ranges[k]}')
            break
    else:
        print(f'Criteria not met for {t}')
```