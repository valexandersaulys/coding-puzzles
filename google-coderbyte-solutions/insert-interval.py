#! usr/bin/python3
"""
This is a common interview question where the input is a sorted list
of disjoint intervals, and your goal is to insert a new interval and
merge all necessary intervals returning a final new list. For example,
if the interval list is [[1,5], [10,15], [20,25]] and you need to
insert the interval [12,27], then your program should return the new
list: [[1,5], [10,27]]. 

Algorithm
(1) create an array where the final intervals will be stored
(2) push all the intervals into this array that comes before the new interval you are adding
(3) once we reach an interval in htat comes after the new interval, add our new interval to the final array
(4) from this point, check each remaining element in the array and determine if the intervals need to be merged
"""

def interval_check(intervals,insert,final=[]):
    for interval in intervals:
        # clean case
        if (interval[0] < insert[0]) and (interval[1] < insert[0]):
            final.append(interval)
        # overlap on the low end
        elif (interval[0] < insert[0]) and (interval[0] < insert[1]):
            going = [interval[0],insert[1]]
            final.append(going)
        elif (interval[0] > insert[0]) and (interval[1] 

