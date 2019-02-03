#! usr/bin/python3
"""
Given an array of strings, return all groups of strings
that are anagrams.

All inputs will be in lower case. 
"""
import string

hash_dict = {s:i for i,s in enumerate(string.ascii_lowercase)}

def char_dict(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d

def homemade_hash(s):
    """Return a simple hash of all the values"""
    return sum([hash_dict[x] for x in s])
    
        

def naive_anagrams(strs):
    """First attempt
    Takes O(n**2) time
    """
    results = [];
    
    for a in strs:
        dict_a = char_dict(a)
        going = []
        for b in strs:
            dict_b = char_dict(b)
            if (dict_a == dict_b) and (a != b) :
                if going == []:
                    going.append(a)
                going.append(b)
        if going != []:
            results.append(going)

    return results 


def anagrams2(strs):
    """Generate hashes of all strings
    see if there are any duplicates

    Takes O(n) time!
    """
    hashes = {}

    for s in strs: # O(n)
        c = homemade_hash(s)  # will assume this is negligible
        if c not in hashes:
            hashes[c] = [s]
        else:
            hashes[c].append(s)

    # O(m) where m is likely less than n above anyway
    results = [v for v in hashes.values() if len(v) > 1]
    return results
        


if __name__ == "__main__":
    print(anagrams2([
        'this',
        'that',
        'tihs'
    ]))
