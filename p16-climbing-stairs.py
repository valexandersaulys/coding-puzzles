#! usr/bin/python3
"""
You are climbing a stair case. It takes n steps to reach the top. 

Each time you can either climb 1 step or 2 steps. In how many distinct
ways can you climb to the top?
"""
def climb_stairs(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1   # take 1 step
    elif n == 2:
        return 2   # take 2 1 steps or 2 steps
    else:
        return climb_stairs(n-1) + climb_stairs(n-2)

def climb_stairs_official(n):
    """This is in the book -- my answer differs slightly"""
    fn2 = 1; fn1 = 2;
    if n == 1:
        return fn2
    elif n == 2:
        return fn1

    fn = 0
    for i in range(3,n+1): 
        fn = fn2 + fn1  # running tally
        fn2 = fn1  # climb_stairs(n-1)
        fn1 = fn   # climb_stairs(n-2)
    return fn


if __name__ == "__main__":
    print("My solution is %d" % climb_stairs(10));
    print("Official solution says %d" % climb_stairs_official(10));
