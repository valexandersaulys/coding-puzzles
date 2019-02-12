#! usr/bin/python3
"""
Construct a function that finds the missing value between
two lists.
"""

def reverse_list(x):    
    i = 0
    j = len(x)-1
    # completes in O(n) time
    while (i < j):
        x[i],x[j] = x[j],x[i]
        i += 1
        j -= 1        
    return ''.join(x)

def reverse_python(x):
    output = [''] * len(x)
    for i,c in enumerate(x):
        output[-1*(i+1)] = c
    return ''.join(output)

def reverse(x):
    output = ['']*len(x)
    i = len(x) - 1
    for c in x:
        output[i] = c
        i -= 1
    return ''.join(output)

def find_missing(arr1, arr2):
    """
    Assume that arr2 has more elements than arr1 and that 
    there is exactly one element missing.

    Brute force is search for each element in arr1 inside of
    arr2. This takes O(mn) time where m is length of arr1
    and n is length of arr2.

    Pythonic: return set(arr2) - set(arr1) really 

    Add all the numbers in both and then substracting the two is
    another one. However, this can potentially result in a very 
    large number. 

    Using XOR... <https://stackoverflow.com/questions/45747177/xor-to-find-the-missing-element-between-two-lists>
      - number ^ number = 0 always
      - number ^ 0 = number
      - order of operations does not matter
    
    
    """
    s = 0;  # this never gets above the missing integer
    for i in arr1:
        s ^= i

    for j in arr2:
        s ^= j

    return s
    
    


if __name__ == "__main__":
    # first question was to implement a reversed array
    #print(reverse('too bad i hid a boot'))

    print(find_missing([1,2,3,4,5,6,7],[3,7,2,1,4,5]))
