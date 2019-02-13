#! usr/bin/python3
"""
Write a function that takes two strings s1 and s2
and returns the longest common subsequence of s1 and s2

These don't always come along in the same order

'ABAZDC', 'BACBAD' => 'ABAD'
'AGGTAB', 'GXTXAYB' => 'GTAB'
'aaaa', 'aa' => 'aa'


Brute Force:
  - Move a pointer along for each sequence. 
  - If I don't have a letter match, move one along until I do. 
  - If I get to a point where I find no common letters, I'll 
    move the second pointer up one.
"""
def longest_common_subsequence(s1,s2):
    """Using memo"""
    if len(s1) < len(s2):
        s1,s2 = s2,s1
    
    m = len(s1)
    n = len(s2)
    candidates = []

    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = '';  # storing the longest length found so far
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + s1[i-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1], key=len )

    return L[m][n], len(L[m][n])

    


def longest_common_subsequence_bad(s1,s2):
    """My first approach"""
    i = 0;   # for s1
    j = 0;   # for s2
    result = ''
    going = ''

    print("%s - %s" % (s1,s2))
    while i < len(s1) and j < len(s2):
        print("%d\t%d\t%s\t%s\t%s" % (i,j,s1[i],s2[j],going))
        if s1[i] == s2[j]:
            #print("%d\t%d\t%s\t%s\t%s" % (i,j,s1[i],s2[j],going))
            going += s1[i]
            i += 1
            j += 1
        else:
            j += 1

            if j == len(s2):
                j = 0
                i += 1
                going = ''


        if len(going) > len(result):
            result = going

    return result
        
        

    

if __name__ == "__main__":
    print(longest_common_subsequence(s1='ABAZDC',
                                     s2='BACBAD'))

    print(longest_common_subsequence(s1='AGGTAB',
                                     s2='GXTXAYB'))

    print(longest_common_subsequence(s1='aaaa',
                                     s2='aa'))

    print(longest_common_subsequence(s1='ABBA',
                                     s2='ABCABA'))

