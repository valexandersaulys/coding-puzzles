#! usr/bin/python3
"""
Find _all_ pairs of two intergers that add to S.

a + b = S


> Bonus: can you do this with triplets?
"""
def construct_hash(lArray, S): 
    d = {}
    for i in lArray:
        if i not in d:  # no repeats assumed here! -- suppose it wouldn't matter
            d[S-i] = i
    return d


def two_sum(lArray, S):
    # assumption that lArray has _no_ repeats
    d = construct_hash(lArray,S);  # O(n)
    results = [];
    
    for i in lArray:  # O(n)
        if i in d:
            results.append((i,d[i]))

    return results;


if __name__ == "__main__":
    print(two_sum(
        [3, 5, 2, -4, 8, 11],
        7
    ))
