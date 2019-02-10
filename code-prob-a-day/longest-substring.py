#! usr/bin/python3
"""
Good morning! Here's your coding interview problem for today. 

This problem was asked by Amazon.
 
Given an integer k and a string s, find the length of the longest
substring that contains at most k distinct characters. 

For example, given s = "abcba" and k = 2, the longest substring with k
distinct characters is "bcb". 

Upgrade to premium and get in-depth solutions to every problem. Since
you were referred by one of our affiliates, you'll get a 10% discount
on checkout! 

If you liked this problem, feel free to forward it along so they can
subscribe here! As always, shoot us an email if there's anything we
can help with! 
"""
import time
import string
import random

def unique_char_count(s):
    # we can assume this take O(n) time?
    return len(set(s))  # simplest solution in pure python

def naive_longest_substring(k,s):
    """
    Takes O(n^3) time with two intersecting loops and the unique count

    s: substring given
    k: integer of at most distinct characters
    """
    longest_substring = '';
    length_substring = 0;
    ucs = 0;
    l = len(s)

    for i in range(l):
        for j in range(i,l+1):
            ss = s[i:j]
            if unique_char_count(ss) > k:
                break
            elif (j-i+1 > length_substring):
                longest_substring = ss
                length_substring = len(ss)
                ucs = unique_char_count(ss)

    return longest_substring,length_substring

def longest_substring(k,s):
    longest_substring = '';
    length_substring = 0;
    ucs = 0;
    length_of_passed_string = len(s);

    """
    Use unique_chars to store a list of unique characters so far.
    Add to it if we increase one way, remove from it if we pass the k
    """

    i = 0 # count the left end
    j = 1 # count the right end
    unique_chars = [s[0]] 

    while j < length_of_passed_string:
        #print("%s thru %s" % (i,j))
        #print("%s with %d unique chars" % (s[i:j],len(unique_chars)))
        if (s[j] not in unique_chars):
            unique_chars.append(s[j])

        # if we have too many unique characters, we increment i and remove from unique_chars
        if len(unique_chars) > k:
            i += 1
            if (s[i-1] in unique_chars) and (s[i-1] not in s[i:j]):
                unique_chars.remove(s[i-1])
        elif (len(s[i:j+1]) > length_substring):
            #print("new record!")
            length_substring = len(s[i:j+1])
            longest_substring = s[i:j+1]
        else:
            j += 1

    return longest_substring, length_substring
                

if __name__ == "__main__":
    # a few examples
    #print(longest_substring(2,'abcba')==naive_longest_substring(2,'abcba'))
    #print(naive_longest_substring(3,'adbcbabbbbbba')==longest_substring(3,'adbcbabbbbbba'))

    # random number of characters to better time it
    sequence_to_do = ''.join([string.ascii_lowercase[random.randint(0,25)] for _ in range(10000)])
    #sequence_to_do = 'vuqoozpbmqrjqhfsqqnpkquoaabayjozejivklikmcbjdghraxaegxebfyrrbpephynwcqfzjutxlzdkvbihljjmoyaiclximfp'
    #sequence_to_do = 'rrbpep'
    print(sequence_to_do)
    start_time = time.time()
    print(naive_longest_substring(k=3,s=sequence_to_do))
    print("Took %0.5f seconds in naieve" % (time.time()-start_time))

    start_time = time.time()
    print(longest_substring(k=3,s=sequence_to_do))
    print("Took %0.5f seconds in better version" % (time.time()-start_time))
