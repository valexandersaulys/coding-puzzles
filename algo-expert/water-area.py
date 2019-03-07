#! usr/bin/env python3
def waterArea(heights):
    max_height = float('-inf')
    max_i = -1
    valleys = []
    last_valley_i = -1
    running_area = 0

    for i,current_height in enumerate(heights):
        if current_height >= max_height and current_height != 0:   # >=?
            # if we haven't initialized yet, set it and continue
            if max_height == float('-inf') and max_i == -1:
                max_height = current_height
                max_i = i
                continue
            
            # we perform a calculation of the area minus past issues
            calc_width = i - max_i - 1
            calc_height = max_height  # we want the "current" max height
            valley_subtraction = sum(valleys)  # all are width 1 so 1xheight added up
            running_area += calc_width*calc_height - valley_subtraction
            
            valleys = []
            max_height = current_height
            max_i = i
        elif len(valleys) > 1 and current_height < valleys[-1]:
            # if I have valleys and my new valley is smaller than my last valley
            # calculate against the last valley and up until that point
            calc_width = last_valley_i - max_i - 1
            calc_height = valleys[-1]
            valley_subtraction = sum(valleys[:-1])
            running_area += calc_width*calc_height - valley_subtraction

            # set the new max height to the last valley, add the new point to
            # valleys, empty everything else
            max_height = valleys[-1]
            max_i = last_valley_i
            valleys = [current_height]
            last_valley_i = i
        elif current_height < max_height and current_height != 0:
            # if we're at a non-zero point, the result is a valley
            valleys.append(current_height)
            last_valley_i = i
        elif current_height < 0:
            # apparently we can have subterranean walls -- does this matter?
            pass

    if valleys and last_valley_i != i:
        calc_width = last_valley_i - max_i - 1
        calc_height = min(max_height, valleys[-1])
        valley_subtraction = sum(valleys[:-1])
        
        running_area += calc_width*calc_height - valley_subtraction

    return running_area



def waterArea(heights):
    max_height = float('-inf')
    max_i = -1
    valleys = []   # will hold tuples of (index,height)
    running_area = 0

    for i,current_height in enumerate(heights):
        if current_height >= max_height and current_height != 0:   # >=?
            # if we haven't initialized yet, set it and continue
            if max_height == float('-inf') and max_i == -1:
                max_height = current_height
                max_i = i
                continue
            
            # we perform a calculation of the area minus past issues
            calc_width = i - max_i - 1
            calc_height = max_height  # we want the "current" max height
            valley_subtraction = sum(x[1] for x in valleys)  # all are width 1 so 1xheight added up
            running_area += calc_width*calc_height - valley_subtraction
            
            valleys = []
            max_height = current_height
            max_i = i
        elif current_height < max_height and current_height != 0:
            # if we're at a non-zero point, the result is a valley
            valleys.append((i,current_height))

    print(valleys)

    if valleys and max(x[1] for x in valleys) == valleys[-1][1]:
        # if we have valleys and our last valley was the greatest
        last_valley_i, last_valley_height = valleys[-1]
        calc_width = last_valley_i - max_i - 1
        calc_height = min(max_height, last_valley_height)
        valley_subtraction = sum(x[1] for x in valleys)
        running_area += calc_width*calc_height - valley_subtraction

    return running_area


def waterArea2(heights):
    maxes = [0 for _ in heights]
    # iterate finding the maxes from the left to right as out default fill
    leftMax = 0
    for i,height in enumerate(heights):
        maxes[i] = leftMax
        leftMax = max(leftMax, height)

    # iterate finding the heights from right to left, subtracting for when we
    # find points lower than our total fill
    rightMax = 0
    for i,height in reversed(list(enumerate(heights))):
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)

    print(maxes)
    return sum(maxes)


def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)

    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)

    print(maxes)
    return sum(maxes)


if __name__ == "__main__":
    #print(waterArea(heights=[0,0,8,0,0,5,0,0]))
    print(waterArea(heights=[0,8,0,0,5,0,0,10,0,0,1,1,0,3]))
    print(waterArea2(heights=[0,8,0,0,5,0,0,10,0,0,1,1,0,3]))    
    #print(waterArea(heights=[0,100,0,0,10,1,1,10,1,0,1,1,0,100]))
    #print(waterArea(heights=[0,100,0,0,10,1,1,10,1,0,1,1,0,0]))  # this won't solve this case ugh
