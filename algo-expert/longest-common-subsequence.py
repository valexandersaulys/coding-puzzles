def longestCommonSubsequence(str1, str2):
    # construct our array for Dynamic Programming
    if str1 == "" or str2 == "":
        return []
    
    DP = [ [ (0,[]) for _ in range(len(str2)) ] for _ in range(len(str1)) ]
    # Iterate through it
    for r,row in enumerate(DP):              # iterate over the first string
        for c,col_value in enumerate(row):   # iterate over the second string
            up = DP[r-1][c] if r-1 >= 0 else (0,[]); 
            left = DP[r][c-1] if c-1 >= 0 else (0,[]);
            DP[r][c] = max(up,left,key=lambda x: x[0])
            
            if str1[r] == str2[c]:
                tmp = DP[r-1][c-1] if (r > 0 and c > 0) else (0,[])
                DP[r][c] = (tmp[0]+1, tmp[1] + [str1[r]])


    print(DP)
    
    return DP[-1][-1][1]


            


if __name__ == "__main__":
    print(longestCommonSubsequence('', ''))
    print(longestCommonSubsequence('YXXXYZ', 'XXXPOADF'))
	
