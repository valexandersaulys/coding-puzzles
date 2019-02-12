#! usr/bin/python3
"""
Find all pairs that add up to K
"""
def find_all_pairs(arr,k):
    """
    Done in O(n) space and O(n) time complexity 

    Assumptions:
      - not ordered!
    """
    d = {}
    sets = []

    # construct dictionary
    for a in arr:
        if a not in d:
            d[k-a] = a

    # run through array to see if it exists already
    for a in arr:    # duplicates will pop up here if they exist!
        if a in d:
            sets.append((a,d[a]))
            # eliminate key if found 
            #del d[a]

    return sets   # alternatively, wrap this in set to eliminate duplicates


if __name__ == "__main__":
    print(find_all_pairs(arr=[1, 2,3, 2,3, 3,2, 5,46,6,7,4],
                         k=5))
