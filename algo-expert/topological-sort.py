#! usr/bin/env python3
from typing import List

def topologicalSort(jobs: List[int], deps: List[ List[int] ]):
    relies_upon = {}   # { job_number: [pre-req jobs...] }

    if deps == [] or deps == [[]]:
        return jobs
    
    # build base values in our dictionary -- O(J)
    for job in jobs:
        relies_upon[job] = []

    # add dependencies -- second job relies on the first job, first must be done before second
    # O(D)
    for x,y in deps:
        relies_upon[y].append(x)
        
    results = []
    while relies_upon:
        #print(relies_upon)
        job_to_remove = None
        
        # find an empty list -- no pre-reqs
        for k,v in relies_upon.items():
            if v == []:
                print("k=%r" % k)
                relies_upon.pop(k,None)  # remove the key from dictionary
                job_to_remove = k
                print(job_to_remove)

                if relies_upon == {0: [], 10: [], 11: [10], 12: [11]}:
                    print("job_to_remove=%r" % (job_to_remove))
                
                results.append(k)
                break

        # didn't find an empty list
        if job_to_remove is None:
            print("no job to remove")
            return []

        # modify the existing dictionaries to remove our first job
        for k,v in relies_upon.items():
            if job_to_remove in v:
                relies_upon[k].remove(job_to_remove)

    return results;
        



if __name__ == "__main__":

    print(topologicalSort(
        jobs = list(range(12+1)),
        deps = [
            [1,2], [1,3], [1,4], [1,5], [1,6], [1,7],
            [2,8], [3,8], [4,8], [5,8], [6,8], [7,8],
            [2,3], [2,4], [5,4], [7,6], [6,2], [6,3],
            [6,5], [5,9], [9,8], [8,0], [4,0], [5,0],
            [9,0], [2,0], [3,9], [3,10], [10,11], [11,12], [2,12]
        ]))
    
    # example given
    #print(topologicalSort(jobs=[1,2,3,4], deps=[[1,2], [1,3], [3,2], [4,2], [4,3]]))

    # base case of having only 1 job
    #print(topologicalSort(jobs=[1],deps=[[]]))

    # case of having 2 jobs with 1 dependencie
    #print(topologicalSort(jobs=[1,2], deps=[[2,1]]))

    # case of having no possible order
    #print(topologicalSort(jobs=[1,2,3], deps=[[3,1],[2,3],[1,2]]))
