#! usr/bin/env python3

def largestRange(array):
    """
    A _range_ is defined as a set of numbers such that the numbers 
    come right after each other inclusive. 
    
    Ex. [2,3,4,5,6] is represented by [2,6] output.
    Ex. [1,11,3,0,15,5,2,4,10,7,12,6] => [0,7] via [1,3,0,5,2,4,7,6] in the array, in order


    Total Time: O(nlogn)
    Total Space: constant
    """
    tmp = sorted(array)  # O(nlogn)
    print(tmp)
    #start, end = 0, len(tmp)-1
    i,j = 0,0
    longest_so_far = 0
    results = []

    # O(n) time
    while j < len(tmp)-1:
        if tmp[j]+1 == tmp[j+1] or tmp[j] == tmp[j+1]:
            #print(longest_so_far)
            j += 1
            if j-i >= longest_so_far:
                longest_so_far = j-i
                results = [tmp[i], tmp[j]]
        else:
            i = j+1
            j = i

    return results



def largestRange(array):
    """
    Ideal is O(n) time and O(n) space (!!)
    """
    print(array)
    longest_so_far = 0
    x,y = None, None
    
    # Hash it
    nums = {}
    for a in array:
        nums[a] = True

    # for each number
    for a in array:
        # continue if not in hash
        if not nums[a]:
            continue
        
        # otherwise, take it and loop through all numbers before and after ascending by one
        nums[a] = False
        left = a-1
        right = a+1
        while nums.get(left,False):
            nums[left] = False
            left -= 1
        while nums.get(right,False):
            nums[right] = False
            right += 1
            
        # record the lengths, return the longest one
        if right - left > longest_so_far:
            x,y = left+1,right-1
            longest_so_far = right-left

    return [x,y]
            

if __name__ == "__main__":
    print(largestRange([1]))
    print(largestRange(list(range(2,6+1))))
    print(largestRange([2,3,4,9,15,17]))
    print(largestRange([1,11,3,0,15,5,2,4,10,7,8,6]))
    print(largestRange([1,3,0,5,2,4,7,6]))

    print(largestRange(list(range(-7,8)) + [1,2,3]))
    print(largestRange([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]))  # should be [-7,7]
    


