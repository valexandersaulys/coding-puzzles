#! usr/bin/python3
"""
Given a set of candidate numbers C and a target number T, find all
unique combinations in C where the candidate numbers sum to T. 

The _same_ repeated number may be chosen from C unlimited number 
of times.

https://stackoverflow.com/questions/3099987/generating-permutations-with-repetitions-in-python
"""
def product(*args, repeat=1):
    """https://docs.python.org/3/library/itertools.html#itertools.permutations"""
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def combinations_no_replacement(iterable, r):
    """r is length of subsets"""
    pool = tuple(iterable) # turn this into tuples for output
    n = len(pool)

    # if we're looking for subsets larger than total avaiable, we skip
    if r > n:  
        return

    # first we return all subsets of size 1 
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)

    # then we go and return all subsets of size 2+
    while True:
        # start with the largest values(?)
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
            else:
                return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def find_all_sets(C=[],T=0,results=[]):
    """This will get recursively called"""
    print("C: %r, T: %d" % (C,T))
    if T < 0:
        return;
    if sum(C) == T:
        return C

    for i in range(len(C)):
        results.append( find_all_sets(C[:i]+C[i+1:],
                                      T=T) )
    return results


def get_all_combations(C,l=None,results=[]):
    if l == None:
        l = len(C)
    elif l <= 0:
        return results;
        
    for i in range(l):
        results.append(get_all_combations(C,l=i,results=results))

    return results



def combination_sum(candidates,target):
    results = []
    solutions = []
    s = 0  # sums
    candidates.sort()  # reverse?
    results = get_combinations(candidates, s, 0, target, solutions, results)
    return results
    
def get_combinations(candidates, s, level, target, solutions, results):
    if s > target:
        return [];
    if s == target:
        results.append(solutions)
        return results;
    i = level
    while i < len(candidates):
        s += candidates[i]
        solutions.append(candidates[i])  # solutions is supposed to be a pointer ugh
        solutions = get_combinations(candidates, s, i, target, solutions, results)
        #solutions.pop()
        s -= candidates[i]
        i += 1
    return results


if __name__ == "__main__":
    #print(find_all_sets([2,3,6,7],7));
    print(combination_sum([2,3,6,7],7))
    #print(get_all_combations([1,2]))
