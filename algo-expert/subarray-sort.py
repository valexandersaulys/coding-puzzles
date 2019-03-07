#! usr/bin/env python3

def subarraySort(array):
    i = 0
    j = len(array)-1

    print("array[i]\tarray[j]\tcenter_min\tcenter_max")
    
    while i <= j:
        
        # O(n) time operation
        center_max = max(array[i+1:j])
        center_min = min(array[i+1:j])

        if array[i] >= center_min and array[j] <= center_max:
            return [i, j]

        print("%d\t\t%d\t\t%d\t\t%d" % (array[i],array[j],center_min,center_max))

        if array[i] < center_min:
            i += 1

        if array[j] > center_max:
            j -= 1
	
    return [-1, -1]


def subarraySort(array):
    i = 0
    j = len(array)-1
    while i < j:
        # O(n) time operation
        center_array = array[i+1:j]
        if center_array != []:
            center_max = max(center_array)
            center_min = min(center_array)
        else:
            if array[j] >= array[i]:
                return [-1,-1]
            else:
                return [i,j]
		
        if not (array[i] <= center_min) and not (array[j] >= center_max):
            return [i, j]
		
        if array[i] <= center_min:
            print(center_array)
            i += 1
			
        if array[j] >= center_max:
            j -= 1

    print("%d,%d" % (i,j))
    if i > j:
        return [-1, -1]
    else:
        return [i-1,j]

    
def subarraySort(array):
    minOOO = float('inf')
    maxOOO = float('-inf')
    for i,x in enumerate(array):
        if is_out_of_order(i,x,array):
            minOOO = min(minOOO,x)
            maxOOO = max(maxOOO,x)

    if minOOO == float('inf'):
        return [-1,-1]
            
    i,j = 0,len(array)-1
    while i < j:
        if array[i] > minOOO:
            break;
        i += 1

    while i < j:
        if array[j] < maxOOO:
            break
        j -= 1
    return [i,j]


def is_out_of_order(i,x,array):
    if i == 0:
        return not (x <= array[i+1])
    if i == len(array)-1:
        return not (x >= array[i-1])
    return not (x <= array[i+1]) or not (x >= array[i-1])


if __name__ == "__main__":
    print(subarraySort([1,2,4, 7,10,11,7,12,6,7, 16,18,19]))
    print(subarraySort([1,2,4,7, 10,11,7,12,7,7, 16,18,19]))
    print(subarraySort([2,1]))
    print(subarraySort([1,2]))
