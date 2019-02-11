#! usr/bin/python
"""
Sort an array of 0,1,2 in linear time with no extra space
"""
def dutch_sort(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while (mid < len(arr)) and (mid < high):
        if arr[mid]==1:
            mid += 1
            continue
        elif arr[mid]==0:
            arr[low],arr[mid] = arr[mid],arr[low];
            low += 1
        elif arr[mid]==2:
            arr[high],arr[mid] = arr[mid], arr[high];
            high -= 1
        mid += 1

    return arr;


if __name__ == "__main__":
    print(dutch_sort([2,0,0,1,2,1]))
