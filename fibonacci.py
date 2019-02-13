#! usr/bin/python3
import sys
from time import time

def fibonacci_naive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci(n,memo={1:0,2:1}):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)
    return memo[n]


if __name__ == "__main__":
    start_time = time()
    print(fibonacci_naive(int(sys.argv[1])));
    print("Took %0.6f" % (time()-start_time))

    start_time = time()
    print(fibonacci(int(sys.argv[1])));
    print("Took %0.6f" % (time()-start_time))
