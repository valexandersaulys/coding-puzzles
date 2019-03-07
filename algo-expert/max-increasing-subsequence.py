#! usr/bin/env python3

def maxSumIncreasingSubsequence(array):
    max_sums = [0] * len(array)
    max_subsequences = [[]] * len(array)
    ret_index = 0
    
    for i,x in enumerate(array):
        # at each point, we add all values before that are less than our current value
        running_number = array[i]
        #running_subseq = [None] * (i+1)
        running_subseq = []
        
        j = 0
        while j < i:
            if array[j] < array[i] and array[i]+max_sums[j] > running_number:
                running_number = array[i] + max_sums[j]
                running_subseq = list(max_subsequences[j])
            j += 1
            
        running_subseq.append(array[i])

        # append this to our lists
        max_sums[i] = running_number
        max_subsequences[i] = running_subseq

        if max_sums[i] > max_sums[ret_index]:
            ret_index = i
        

    print(max_sums)
    print(max_subsequences)
            
    return max_sums[ret_index], [x for x in max_subsequences[ret_index] if x != None]
            
         
    


if __name__ == "__main__":
    #print(maxIncreasingSubsequence([8,12,2,3,15,5,7]))
    #print(maxIncreasingSubsequence([10,70,20,30,50,11,30]))
    #print(maxIncreasingSubsequence([-1,1]))
    print(maxIncreasingSubsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))
