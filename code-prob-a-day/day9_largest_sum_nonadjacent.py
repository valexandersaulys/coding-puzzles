#! usr/bin/python3
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest
sum of non-adjacent numbers. Numbers can be 0 or negative. 

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and
5. [5, 1, 1, 5] should return 10, since we pick 5 and 5. 

Follow-up: Can you do this in O(N) time and constant space? 
"""

def my_largest_sum(arr: list):
    """
    This is constant space and constant time
    """
    if max(arr[-2:]) > max(arr[:2]):
        arr.reverse()  # I'm gonna assume this is constant space operation
    i = 0
    running_sum = 0
    while i+1 < len(arr):
        print("Comparing => %d\t%d" % (arr[i],arr[i+1]))
        if arr[i] >= arr[i+1]:
            if arr[i] < 0:
                i += 2
                continue
            running_sum += arr[i]
            i += 2
        elif arr[i] < arr[i+1]:
            if arr[i] < 0:
                i += 3
                continue
            running_sum += arr[i+1]
            i += 3

    if i < len(arr):
        print("Last Value => %d" % arr[i])
        if not arr[i] < 0:
            running_sum += arr[i]

    return running_sum


def largest_sum(arr: list):
    incl = 0
    excl = 0
    #switch = False

    for i,x in enumerate(arr):
        # new_excl will be the old excl if its greater than the prior
        # included or the prior included as it can't include the
        # current element. 
        new_excl = excl if excl > incl else incl
        incl = excl + x  # max sum including the past element
        excl = new_excl  # max sum excluding the past element

    return max(incl,excl)


if __name__ == "__main__":
    print(largest_sum(arr=[5,1,1,5]))
    #print(largest_sum(arr=[2,4,6,2,5]))
    #print(largest_sum(arr=[5,-1,-1,5,7]))
    #print(largest_sum(arr=[7,-1,-1,-1,-1]))

    print(largest_sum(arr=[1,2,3]))
    print(largest_sum(arr=[1,20,3]))
    print(largest_sum(arr=[5,5,10,100,10,5]))

