#! usr/bin/env
"""
"""
def smallestDifference(arrayOne, arrayTwo):
    # O(nlogn) sort here
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne);
    print(arrayTwo);

	# binary search using one array
    for a in arrayOne:
        # binary search for lowest value O(n)
        tmp = arrayTwo
        best_so_far = None   # will hold a tuple
        while tmp:
            i = len(tmp) // 2
            b = tmp[i]

            if a == 25:
                print("%d,%d" % (a,b))
                print(best_so_far)

            if not best_so_far or ( abs(a-b) < abs(best_so_far[0]-best_so_far[1]) ):
                best_so_far = [a,b]

            if a > b:
                tmp = tmp[i:] if i != 0 else []  # look right
            else:
                tmp = tmp[:i] if i != 0 else []  # look left

    return best_so_far

if __name__ == "__main__":

    print(smallestDifference(
        [10,0,20,25,2200],
        [1005,1006,1014,1032,1031]
    ))
