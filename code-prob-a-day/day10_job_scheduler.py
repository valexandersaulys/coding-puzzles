#! usr/bin/python3
"""

"""
from time import sleep
from threading import Thread


def wait_before_execute(f,n,args=()):
    sleep(n/1000)  # to get it in milliseconds
    f(args)



if __name__ == "__main__":
    f = lambda x: print(x**8);
    wait_before_execute(f,n=1000,args=(2))
