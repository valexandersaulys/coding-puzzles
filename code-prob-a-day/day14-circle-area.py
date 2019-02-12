#! usr/bin/python3
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal
places using a Monte Carlo method. 

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random
import math

def monte_carlo_circle(Cx=1,Cy=1,radius=1,X=100):
    Y = 0
    for _ in range(X):
        # generate a random point
        x = random.random()
        y = random.random()
        
        # its in the circle, count it
        if math.sqrt((x-Cx)**2 + (y-Cy)**2) <= radius:
            Y += 1

    # return the ratio of points inside the circle vs outside times the area
    return float(Y/X)*Cx**2


if __name__ == "__main__":
    print(monte_carlo_circle(Cx=1,Cy=1,radius=1,X=100000))
    print("Real Area is %0.5f" % (math.pi*0.5**2))
