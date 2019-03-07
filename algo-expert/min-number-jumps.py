#! usr/bin/env python3

def minNumberOfJumps(array, jumps_taken=None, best_so_far=None):
    if array == []:  # we hit the end
        #print('return empty: %d' % jumps_taken)
        return jumps_taken
    
    if not jumps_taken: # to start
        jumps_taken = 0

    if not best_so_far:
        best_so_far = float('inf')

    for i,x in enumerate(array):    
        for j in range(1,x+1):


            
            if i == j:
                continue

            # calculate the min number of jumps from here
            tmp = minNumberOfJumps(array[i+j:],
                                   jumps_taken=jumps_taken+1,
                                   best_so_far=best_so_far)

            if len(array) == len([3,4,2,1,2,3,7,1,1,1,3]):
                print("i=%d\tj=%d\ttmp=%0.0f\tarray=%r" % (i,j,tmp,array[i+j:]))

            if tmp < best_so_far:
                best_so_far = tmp

    #print("%d,%r" % (jumps_taken,array))
    
    return best_so_far


def minNumberOfJumps(array):
    """Version using recursive Dynamic Programming"""
    jumps = [float('inf')]*(len(array))
    jumps[0] = 0

    for i in range(1,len(array)):
        # iterate through all points prior to see if any can jump j to i
        for j in range(0,i):
            # if there are sufficient jumps at array[j] to get to i, we can 
            # see if this is a better path or not
            if array[j] >= i - j:  
                jumps[i] = min(jumps[i],    # we either accept what's there
                               jumps[j]+1)  # or take what's at pos j (jumps to get there) plus
                                            # 1 to account for the new jump
    return jumps[-1]


def minNumberOfJumps(array):
    if len(array)==1:
        return 0
    steps = array[0]
    maxReach = array[0]
    jumps = 0
    for i in range(1,len(array)-1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1
    

if __name__ == "__main__":
    print("min jumps => %d" % minNumberOfJumps([1]))
    print("")
    print("min jumps => %d" % minNumberOfJumps([2,1,1]))
    print("")
    print("min jumps => %d" % minNumberOfJumps([3,4,2,1,2,3,7,1,1,1,3]))
