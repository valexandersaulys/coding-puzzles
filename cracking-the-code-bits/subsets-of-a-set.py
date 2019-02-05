#! usr/bin/python3
"""
Take an array of unique items and return all possible subsets of 
that array.

This should be 2**n subsets.
"""
def subsets_of_set(S):
    results = [[]]
    for s in S:
        results.extend([subset+[s] for subset in results])
    return results


def subsets_with_replacement(S,sizes=0):
    """
    I can't get this!
    """
    results = []
    # top loop handles sizes
    for i in range(1,sizes+1):
        # loop handles position for array
        for j in range(i+1):
            # init empty array to hold this combination array
            to_append = [0]*i           
            for s in S:
                to_append[j] = s
        results.append(to_append)
    return results


if __name__ == "__main__":
    #print(subsets_of_set([1,2,3]))
    print(subsets_with_replacement([1,2],2))
