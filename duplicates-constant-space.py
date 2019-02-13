#! usr/bin/python3

def printRepeating(arr, size): 
    results = []
    
    for i in range(0, size):
        #print("%d\t%d\t%d" % (i,arr[i],arr[abs(arr[i])]))
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])] 
        else: 
            results.append(abs(arr[i]))
    return results


def print_repeating_deux(arr):
    """ Never got this to work =>  https://www.geeksforgeeks.org/duplicates-array-using-o1-extra-space-set-2/"""
    n = len(arr)
    results = []
    
    for i,x in enumerate(arr):
        arr[x % n] += n

    for i,x in enumerate(arr):
        if (x % n) > 1:
            results.append(i)

    return results


if __name__ == "__main__":
    print(printRepeating(arr=[1,2,3,1,3,6,6],size=7))
    #print(print_repeating_deux(arr=[1,2,3,1,3,6,6]))
