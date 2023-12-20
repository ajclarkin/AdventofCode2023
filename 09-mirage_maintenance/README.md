# Mirage Maintenance
This was a nice easy one. In fact it felt like part two must have been a trick - but it wasn't. This was reminiscent of a day 1 or 2 challenge from previous years.

## Features
Nested lists.


## Part 1
Make sure that each row input is read into a list of it's own with the values converted to ints. Then for each row at a time we create a new nested list, with each sublist representing the next level of the tree of numbers. I used the technique explained in the challenge; there might have been a better way but this worked fine.


## Part 2
This time we have to manipulate the other side of the list. I kept the code which built up the list we needed but tweaked it to reverse the order (since I already hhave code for inserting a new value at the right of each list). Then all I had to do was subtract rather than add.
