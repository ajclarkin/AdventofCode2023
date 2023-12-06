from math import sqrt, floor

lines = [x for x in open('input.txt').read().split('\n')]
input = list()
for l in lines:
    input.append([int(x) for x in l.split()[1:]])

values = list()
total = 1


'''
    This is a quadratic. We have a total duration. Each unit of time spent charging becomes a unit of speed
    to use in the remaining time.

    distance travelled = chargetime * remaining time
                       = chargetime * (total time - charge time)
    
    y = distance, x = charge time (because we want to consider variations in this)
    k = total time

    y = kx - x^2

    And then to find the values for x where y > previous record (r) we subtract r to make the roots the cutoff

    y = kx - x^2 - r 


    FOR ROOTS:
        kx - x^2 - r = 0        multiple both sides by -1 to make the coefficients nicer
                                this won't change the roots

'''


for duration, distance in zip(input[0], input[1]):
    r1 = (duration - sqrt((duration * duration) - (4 * 1 * distance))) / (2)
    r2 = (duration + sqrt((duration * duration) - (4 * 1 * distance))) / (2)

    values.append(floor(r2) - floor(r1))
    print(r1, r2)

for v in values:
    total *= v
print(f'The final total is {total}')