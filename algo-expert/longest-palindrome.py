#! usr/bin/env python3

def longestPalindromicSubstring(string):
    """ approach 1"""
    left_pointer = 0
    right_pointer = len(string)-1
    switch = False

    while left_pointer <= right_pointer:
        print("%d\t%d\t%s" % (left_pointer,right_pointer,string[left_pointer:right_pointer+1]))
        
        if string[left_pointer] == string[right_pointer]:
            i = int(left_pointer)
            j = int(right_pointer)

            while string[i] == string[j] and i < j:
                i += 1
                j -= 1
                
                if i >= j:  # they overlapped -- palindrome found
                    return string[left_pointer:right_pointer+1]
                
        if switch:
            left_pointer += 1
        else:
            right_pointer -= 1

        switch = not switch
	        
    return ''


def longestPalindromicSubstring(string):
    """Assumption (from problem): there will be only __one__ palindromic sequence"""
    if len(string) == 1:
        return string
    
    left_pointer = 0
    right_pointer = 1
    candidates = []
    
    while left_pointer < len(string)-1:

        if string[left_pointer] == string[right_pointer]:
            i = int(left_pointer)
            j = int(right_pointer)

            while string[i] == string[j] and i < j:
                i += 1
                j -= 1
                
                if i >= j:  # they overlapped -- palindrome found
                    candidates.append(string[left_pointer:right_pointer+1])
                    break # break out of while loop

        if right_pointer == len(string)-1:
            left_pointer += 1
            right_pointer = left_pointer
            
        right_pointer += 1

    return '' if candidates == [] else \
        [c for c in candidates if len(c) == max(len(x) for x in candidates)]
        

if __name__ == "__main__":

    print(longestPalindromicSubstring('abaxyzzyxf'))
