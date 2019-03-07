#! usr/bin/env python3

"""
# old recursive way
def diskStacking(disks):
    #memo = [0] * int(len(disks)+1)
    A = helper(disks=disks)

    return A

def helper(disks, existing_stack=[]):
    if disks == []:   # no more disks to add
        return existing_stack
    
    best_stack = existing_stack  # to hold our current best stack

    
    for disk in disks:
        tmp_disks = list(disks)
        tmp_disks.remove(disk)

        tmp_stack = list(existing_stack)
        if tmp_stack != [] and not A_less_than_B(disk, tmp_stack[0]):
            continue;  # continue with the for loop if our disk can't be added
        tmp_stack.insert(0, disk)    

        ret_stack = helper(disks=tmp_disks, existing_stack=tmp_stack)

        if ret_weight(ret_stack) > ret_weight(best_stack):
            best_stack = ret_stack

    return best_stack

def A_less_than_B(A,B):
    return A[0] < B[0] and A[1] < B[1] and A[2] < B[2]

def ret_weight(stack):
    # returns the total height using the third value in the list of lists
    running_weight = 0
    for _,_,weight in stack:
        running_weight += weight
    return running_weight
"""


def diskStacking(disks):
    #memo = [0] * int(len(disks)+1)
    max_heights = [[]]*(len(disks)+1)
    
    for i,disk in enumerate(disks):
        print(">>disk=%r" % disk)
        max_heights[i+1] = helper(disks=list(disks),
                                  existing_stack=[disk],
                                  max_heights=list(max_heights),
                                  disks_to_remove=[disk])

    print(max_heights)

    return max(max_heights, key=ret_weight);

def helper(disks: list, max_heights: list, existing_stack: list, disks_to_remove=[]):

    if disks == []:   # no more disks to add
        return existing_stack
    
    best_stack = existing_stack  # to hold our current best stack

    for i,disk in enumerate(disks):
        # if we're marking it to not check, skip
        if disk in disks_to_remove:
            continue
        
        tmp_disks_to_remove = list(disks_to_remove)
        tmp_disks_to_remove.append(disk)

        tmp_stack = list(existing_stack)
        if tmp_stack != [] and not A_less_than_B(disk, tmp_stack[0]):
            continue;  # continue with the for loop if our disk can't be added
        tmp_stack.insert(0, disk)

        if max_heights[i+1] != []:
            print("disks_to_remove=%r\tdisk=%r\tdisks=%r" % (disks_to_remove,disk,disks))
            # what if my current disk is already in the max_height? skip?
            ret_stack = max_heights[i+1] + existing_stack  
            if ret_weight(ret_stack) > ret_weight(best_stack): best_stack = ret_stack
            continue

        ret_stack = helper(disks=list(disks),   # need to pass in our full list
                           existing_stack=tmp_stack,
                           max_heights=list(max_heights),  # python and pointers man
                           disks_to_remove=tmp_disks_to_remove)

        if ret_weight(ret_stack) > ret_weight(best_stack):
            best_stack = ret_stack

    return best_stack

def A_less_than_B(A,B):
    return A[0] < B[0] and A[1] < B[1] and A[2] < B[2]

def ret_weight(stack):
    """returns the total height using the third value in the list of lists"""
    running_weight = 0
    for _,_,weight in stack:
        running_weight += weight
    return running_weight
        


if __name__ == "__main__":
    # some base cases to try out
    #print(diskStacking([[1,1,1]]))
    
    #print(diskStacking([[1,1,1],[2,2,2]]))
    #print(diskStacking([[1,1,1],[2,2,2],[3,3,3]]))

    # test for ordering
    #print(diskStacking([[2,2,2],[1,1,1],[3,3,3]]))

    # test for non-sequential
    #print(diskStacking([[2,2,2],[1,1,1],[4,4,4]]))
    print(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5]]))

    
