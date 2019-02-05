#! usr/bin/python3
"""
Print all subsets of a set

input set = [1, 2, 3] 
power set = [[], [1], [2], [3], [1, 2], [2, 3], [1, 3] [1, 2, 3]]
"""
def subsets_of_set(lArray):
    results = [];
    n = 2**len(lArray)   # 2**n total subsets

    for i in range(n):
        going = []
        rep = "{0:b}".format(i)
        while len(rep) < len(lArray):
            rep = '0' + rep;

        for j,x in enumerate(rep):
            if x == '1':
                going.append(lArray[j])
            elif x == '0':
                continue

        results.append(going)

    return results


if __name__ == "__main__":
    print(subsets_of_set([1,2,3]));
    print(subsets_of_set([1,2,3,4]));
    print(subsets_of_set(list(range(1200))));
                
            
    
