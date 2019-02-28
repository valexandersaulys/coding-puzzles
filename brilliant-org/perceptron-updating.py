#! usr/bin/env python
from functools import reduce

def weight_update(w,x,y) -> list:
    assert len(w) == len(w)
    x = [i*y for i in x]       # y_i * x_i
    w_k = [i+j for i,j in zip(w,x)]  # w + ___
    return w_k

def bias_update(b, y) -> float:
    assert isinstance(b, (int,float))
    assert isinstance(y, (int,float))
    return b + y

def perform_estimate(examples,w,b):
    """Returns True if all values are True else False"""
    vals = []
    for y,x in examples:
        estimation = sum([i*j for i,j in zip(x,w)]) + b
        vals.append((estimation < 0 and y < 0) or (estimation > 0 and y > 0))
    return reduce(lambda a,b: a & b, vals)

if __name__ == "__main__":
    w = [0,0]; b = 0;
    examples = [
        # y, (x)
        (1, [-1,1]),
        (-1,[0,-1]),
        (1, [10,1])
    ]
    converged = False
    i = 0; j = 0
    while not converged:
        print("W: %r, b: %0.0f" % (w,b))
        converged = perform_estimate(examples,w,b)
        if converged:
            break;

        # this needs to come back to the one example still not working bleh
        y,x = examples[i]
        w = weight_update(w,x,y)
        b = bias_update(b,y)

        i += 1
        if i > 2:
            i = 0

        if j > 6:
            break
        j += 1
    print("Converged at sum: %0.0f" % (sum(w) + b))
