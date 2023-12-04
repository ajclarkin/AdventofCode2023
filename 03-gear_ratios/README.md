# Gear Ratios

First edge case of the year. It took three days to make an incorrect submission.
The important point in this one is correct use of regex to avoid repeats.


## Features
Regular expressions again
2D coordinates
Combinations


## Part 1
Find every number which is in contact with a (non period) punctuation mark, including diagonals. So, I find the (row, col) coordinate of every punctuation mark. Then I find the coordinate of every valid square surrounding a number. Then I compare the two.

The problem here was on an example like this:
```
........
.24..4..
......*.
```

Running `re.findall(r'\d+')` would return 24 and 4 but then using `re.search(r'4')` to find the position of the second would actually find the first number. (Here I was searching for the values found by `re.findall()` so inserting dynamically into the regex.)

The solution was to use `re.finditer(r'\d+')` which created an iterator of all the matches with their span.


## Part 2
This was actually ok. Find all the stars and find all the numbers beside a star. Then iterate through the possible combinations of numbers to see if two of them are in the set of star positions.

I used `itertools.combinations()` to find all the combinations (not permutations) of numbers to compare.