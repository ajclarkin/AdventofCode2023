# Trebuchet
I just don't feel ready for Advent of Code this year. I was super excited for it a couple of weeks ago and now I'm just not there. I'm not sure how far I'm going to get...


## Part 1
Ok, find zero or more digits in a text string. Convert first and last to a number (1 and 5 becomes 15), then sum them. Some rows have 0 or 1 numbers.

Solution uses a regex to find the first and the last which worked better than finding all of them when there is only 1 (and so both first and last).