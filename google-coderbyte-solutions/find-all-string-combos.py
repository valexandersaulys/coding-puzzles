#! usr/bin/python3
"""
input is a string of 0,1, or ?, where ? is a wildcard that can be 0 or 1. Print
all possible combinations of the resultant string.
"""
def get_all_strings(S,results=[[]]):
    if len(S) == 0:
        return results;
    
    if (S[0]=='1') or (S[0]=='0'):
        for i in range(len(results)):
            results[i].append(S[0]);

    if S[0] == '?':
        # duplicate each array in the existing one into a new array
        for i in range(len(results)):
            results.append(list(results[i]))    # duplicating into the array

        # go one way by appending 0 and another by appending 1
        for i in range(len(results)):
            if i < len(results)/2:
                results[i].append('0')
            else:
                results[i].append('1')
                
    # recursively call with the remaining string and results
    return [''.join(x) for x in get_all_strings(S[1:],results)]

if __name__ == "__main__":
    print(get_all_strings('011?0'))
