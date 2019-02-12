"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1
or 2 steps at a time. Given N, write a function that returns the
number of unique ways you can climb the staircase. The order of the
steps matters. 

For example, if N is 4, then there are 5 unique ways: 

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you
could climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. 

Upgrade to premium and get in-depth solutions to every problem. Since
you were referred by one of our affiliates, you'll get a 10% discount
on checkout! 

If you liked this problem, feel free to forward it along so they can
subscribe here! As always, shoot us an email if there's anything we
can help with! 
"""

def staircase(N=0):
    if N <= 0:
        return 1;
    elif N == 1:
        return 1
    elif N == 2:
        return staircase(N=N-1) + 1; # 1 for doing the two step climb
    else:
        return staircase(N=N-1) + staircase(N=N-2)

def dynamic_staircase(N=0,d={1:1}):
    if N in d:
        return d[N]
    elif N <= 0:
        return 1;
    elif N == 2:
        d[N] = dynamic_staircase(N=N-1,d=d) + 1; # 1 for doing the two step climb
        return d[N]
    else:
        d[N] = dynamic_staircase(N=N-1,d=d) + dynamic_staircase(N=N-2,d=d)
        return d[N]

def variable_staircase(N,X=[1,2],d={0:1,1:1}):
    if N in d:
        return d[N]
    if N < 0:
        return 0;
    else:
        ret = 0
        for x in X:
            s = variable_staircase(N=N-x,X=X,d=d)
            print("%d\t%r\t%d" % (N-x,X,s))
            ret += s
        d[N] = ret
        return ret


if __name__ == "__main__":
    print("=> %s" % staircase(N=4))  
    #print(dynamic_staircase(N=10))

    print("=> %s" % variable_staircase(N=4,X=[1,2]))
