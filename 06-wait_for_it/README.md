# Wait For It
I liked this one. It was a nice bit of maths that wasn't too difficult.

## Features
- quadratic equation
- parsing values

## Part 1
The key here is identifying the quadratic process.

We are given a total time (duration) and a distance that has previously been achieved within that time. We have to charge a boat and each unit of time charged gives it an extra unit of speed. When we stop charging we release it and observe how far it travels in the remaining time.

Charge time = speed.

So:
- A short charge will result in low distance due to slow speed.
- A long charge will result in low distance due to short time remaining.
- Somewhere in the middle will be maximise distance.

This is a U-shaped curve.

The independent variable (x) is the charge time. \
The dependent variable (y) is the distance travelled. \

distance = speed * time \
distance = chargetime * remaining time
distance = chargetime * (total time - chargetime)

y = (duration * charge time) - chargetime^2 \
y = (duration * x) - x^2

We want to know how many values for x yield a y value greater than the distance provided. We could calculate this iteratively but by introducing this value as a constant we can move the curve such that the roots (where it crosses the x-axis) correspond to the x value yielding that distance.

y = -x^2 + (duration * x) - distance \ 
and roots are where y = 0 so we can multiply both sides by -1 just to make the coefficients nicer.

Now we can use the quadratic equation to find the roots.

$$x = \frac{{ - b \pm \sqrt {b^2 - 4ac} }}{{2a}}$$



## Part 2
Re-parse the values to make one large duration and one large distance. Doesn't matter because we're going to use the same approach as above.

I could have hard-coded the values into the code but made it a parsing exercise instead.