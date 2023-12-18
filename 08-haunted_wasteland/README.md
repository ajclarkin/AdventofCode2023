# Haunted Wasteland
This was a nice one. I think I over-complicate the reading and parsing of the input file sometimes. Today the format of the input was:

```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
```

I read it in the usual manner: `input = [x for x in open('example.txt).read().split('\n)]` and then assigned the first line (which is the instructions) to a variable using `input[0]` and the continued the slicing to get the rest of the instructions.

Once again I used regular expressions to pull out the values and then assigned them to a dictionary with the values being tuples.

We need the instructions to repeat as we cycle through them (LRLRLR) and so I created a `cycle()` to cycle through the list of instructions using `next()` to access it.


# Features
Cycle, lowest common multiple, * operator (possibly called splat)

# Part 1
Pretty straightforward. As we cycle through the instuctions we move through the dict of nodes until we finish.

# Part 2
There's always a catch. This time it's multiple paths in parallel and finding the point that they finish at the same time. Simply running through it each time didn't work - I didn't really think it would - so I checked to see if each path reached a Z in a cyclical time frame. It did.

The solution then is to find how many moves to finish each path and then find the lowest common multiple of those values.

I had an iterable of the moves for each path but `math.lcm()` requires the values unpacked like positional arguments. The solution is the * operator to unpack them (in the same way as you would unpack *args on the command line).