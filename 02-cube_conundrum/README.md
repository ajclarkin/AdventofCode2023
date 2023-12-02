# Cube Conundrum
This was easier than yesterday but I'm still super rusty at python.
I used regular expressions again. I'm not sure if this was the best way to solve it or just an availability heuristic. Still, it worked and seemed fairly efficient.


## Features
regex


## Part 1
This section is really about parsing out the values. I could have split each line into lists but it wasn't required.
The answer is the sum of game numbers excluding those where a value exceeded a limit so I just calculated the maximum
sum possible and then deducted the game number if it exceeded the limit. I used regular expressions to pull out the values
from the input and a dictionary as a lookup for the maximum limit.


## Part 2
This was easy today. I made a list of the number of dice of each colour per game and then used `max()` to find the highest.