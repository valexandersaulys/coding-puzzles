def permutations(n,i=0,results=[]):
    # base cases
    if n == []:
        results = []
    elif i == len(n) - 1:
        results.append(n)
    else:
        for j in range(i, len(n)):
            tmp = list(n)
            n[i], n[j] = n[j], n[i]

            print("%d\t%d\t%r\t%r" % (i,i,tmp,n))
            
            # python pointers are wacky -- this forces a copy to be sent
            permutations(
                n=list(n),
                i=i+1,
                results=results
            )

            # swap back
            n[i], n[j] = n[j], n[i]

    return 
		
def getPermutations(array,start=0,end=None):
    results = []

    print("start\ti\tbefore\tafter")
    permutations(array,0,results)
    return results



def perm(n, i):
    if i == len(n) - 1:
        print(n)
    else:
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            perm(n, i + 1)
            n[i], n[j] = n[j], n[i] # swap back, for the next loop


if __name__ == "__main__":
    print(getPermutations([1,2,3]))

    
    print(perm([1,2,3], 0))
