# Sorting Algorithms

Insertion Sort: take elements from the list one by one and insert them
into the correct position of a new sorted list. __O(n^2)__

Selection Sort: in-place sorting in which the minimum value is found
and then swapped to the front, with smaller and smaller sublists being
done. This requires two passes resulting ing __O(n^2)__ though its
space requirements are low.

Merge Sort: the list is split in half recrusively going down. Each
sublist is then compared, at element level, so the other element in a
list and then placed into a final list. This requires O(n) space
complexity, but results in __O(n logn)__ time complexity for
computation.

```python
def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # recursively merge the smaller halves
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0   # counter for left array
        j = 0   # counter for right array
        k = 0   # counter in new array
        while i < len(lefthalf) and j < len(righthalf):
            # if the left half's element is smaller, insert it into the new array
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            # vice-versa to above
            else:
                alist[k] = righthalf[j]
                j += 1
            # increment the new array counter
            k += 1

        # finish out the lefthalf into the array if we're done with the right half
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        # same as above for the righthalf
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print('merging)'
```


Quicksort: Pivot around a partion point in which all values less are put to the left and all values greater are put to the right.

```python
def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
```