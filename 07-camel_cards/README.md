# Camel Cards
This took me ages but not because it was particularly difficult. It's tough trying to get through these while on-call for ICU and
with a toddler at home.

Part 1 was straight-forward once I decided on a data structure. Errors cropped up in part 2 but were easy enough to fix.

Everything's also taking longer because I'm using vim settings in VSCode.


## Features
Bubblesort, nested lists, zipping lists to create dictionary.


## Part 1
Read in the input line by line and then slice it to assign the first and second component to different lists. Then `zip()` that together to form a dictionary of the bids for each hand.

Now iterate through each had and assign to an appropriate nested list depending on the rank of the hand. Use a nested counter to count the number of different repetitions eg 2 pairs, 1 three and 1 pair.

So `card_ranks[0]` will be 5 of a kind, `card_ranks[1]` will be 4 of a kind and so on.

```python
card_ranks = [[],[],[],[],[],[],[]]

```

Once all the cards are in ranks each rank gets sorted using bubble sort according to the rules for this round. We have a list called `precedence` and `precedence.index()` gives the position of each card in this. This is what we compare during bubblesort.

Bubblesort took me ages to get working. I rewrote it a couple of times with the same output. I successfully identified if the cards were in the wrong order and so swapped and then broke out of list but I needed to add the `elif` to break out of the comparisons if they were in the right order and so no action required.


Finally, iterate through all the sorted cards and multiply by then bid saved in the dictionary, adding to total.



## Part 2
A few  changes. J becomes bottom precedence. J also mimics any card(s) in the hand to give it maximal rank. So, AAAAJ would become 5 of a kind, 22JKK becomes full house. J doesn't actually change within the hand though and the sorting is the same as before with the new order of precedence.

When assigning ranks we have to check for the presence of J and assign accordingly. This is simpler than it sounds because whether J is in the majority or minority it has the same effect *most of the time*. For example, AAAJJ or AAJJJ both become 5 of a kind.