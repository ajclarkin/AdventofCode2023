import re

input_groups = [x for x in open('input.txt').read().split('\n\n')]

seeds = [int(x) for x in re.findall('\d+', input_groups.pop(0))]
range_list = list()
soil = list()

# Create a list of dicts
#   Each dict applies to one step in the transformation.
#   The key is the source range and the value is the conversion factor to add to get the destination
for group in input_groups:
    ranges = dict()
    for row in group.split('\n')[1:]:
        dest, source, length = row.split()
        ranges[(int(source), int(source) + int(length) -1)] = int(dest) - int(source)
    range_list.append(ranges)


# Work each seed through the ranges for each stage
# Compare to see if it has a mapping in each of those ranges
# Finally add the transformed seed value to soil
for s in seeds:
    for range in range_list:
        for k in range.keys():
            if k[0] <= s <= k[1]:
                s += range[k]
                break

    soil.append(s)

print(f'The soil locations are:\n{soil}')
print(f'The closest location is :\n{min(soil)}')

