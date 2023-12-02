# Trebuchet
I just don't feel ready for Advent of Code this year. I was super excited for it a couple of weeks ago and now I'm just not there. I'm not sure how far I'm going to get...

## Features
regex


## Part 1
Ok, find zero or more digits in a text string. Convert first and last to a number (1 and 5 becomes 15), then sum them. Some rows have 0 or 1 numbers.

Solution uses a regex to find the first and the last which worked better than finding all of them when there is only 1 (and so both first and last).

`^\D*(\d)` uses caret to identify the start of the string, then 0 or more non-digits then a digit. Putting the digit in brackets causes it to be extracted rather than a full match.


## Part 2
This seemed to cause problems for the pros as well so I don't feel so bad.

Now we need to consider numbers like 'eight' and we also need to allow for overlaps such as 'eightwone'. Standard regular expressions would miss the two in this example. The workaround is to use a lookahead (?=(pattern)).

`(?=(one|two|three|four|five|six|seven|eight|nine|\d))`

I used a dictionary to convert each number to a value `{'one': 1}` but that was overkill - I could have just used a list of the names in order and then used the position in the list.