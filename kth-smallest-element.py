#! usr/bin/python3
"""
Find the kth smallest (or largest) element in an array
"""
def kth_smallest_element(arr,k=0,l=0,r=None):
    if r == None:
        r = len(arr)-1

    if k > 0 and (k <= (r-l+1)):
        # we start with the far right as the position element
        pos = partition(arr,l,r);

        if (pos-l) == (k-1):
            return arr[pos]

        if pos-l > k-1:
            print("must be to left of partition")
            return kth_smallest_element(arr,k=k,l=l,r=pos-1)

        # must be in right of partition
        print("must be to right of partition: %d" % (k-pos+l-1))
        return kth_smallest_element(arr,
                                    k=k-pos+l-1,  # adjust k
                                    l=pos+1,
                                    r=r)
    return False

def partition(arr,l,r):
    """
    move the pivot point to a point where all elements smaller than it
    come before and all elements larger come after
    """
    print("run partition")
    x = arr[r]   # partition element 
    i = l  # position counter for where to put pivot element
    for j in range(l,r):  # j is the position counter on lefthand side
        # swap partition if its greater than the element we're currently at
        if arr[j] <= x:  
            arr[i], arr[j] = arr[j], arr[i]
            i += 1  
    arr[i], arr[r] = arr[r], arr[i]  
    return i
                                    
                                    


if __name__ == "__main__":
    A = kth_smallest_element(arr=[3,7,8,5,2,1,9,4],k=3)
    print(A)
