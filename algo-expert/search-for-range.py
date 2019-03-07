#! usr/bin/env python3
def searchForRange(array, target):
    return sfr_helper(array, target, 0, len(array)-1);


def sfr_helper(array, target, li, ri):
    print("array=%r\ttarget=%d\tli=%d\tri=%d" % (array, target, li, ri))
    if li > ri:
        return [-1, -1]

    mi = (ri+li) // 2
	
    if target == array[mi]:
        if array[mi-1] == target:
            # still need to explore left
            left_start, _ = sfr_helper(array, target, li=li, ri=mi-1)
        else:
            left_start = mi

        if mi < len(array)-1 and array[mi+1] == target:
            # still need to explore right
            _, right_start = sfr_helper(array, target, li=mi+1, ri=ri)
        else:
            right_start = mi

        return left_start, right_start

    elif target < array[mi]:
        # search left, looking for it
        return sfr_helper(array, target, li=li, ri=mi-1)
    elif target > array[mi]:
        # search right, looking for it
        return sfr_helper(array, target, li=mi+1, ri=ri)


if __name__ == "__main__":
    print(searchForRange(array=[0,1,1,1,5,6,11,43,109],target=1))
    print(searchForRange(array=[0,1,21,33,45,45,45,45,45,45,61,71,73],target=45))

    # edge cases where numbers are at the end
    #print(searchForRange(array=[5,6,10,15,23,39],target=29))
    print(searchForRange(array=[5,6,10,15,23,39],target=39))
    #print(searchForRange(array=[0,1,21,33,45,45,45,45,45,45],target=45))
	

