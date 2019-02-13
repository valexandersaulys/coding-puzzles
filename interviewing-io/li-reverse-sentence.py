#! usr/bin/python3

def reverse_sentence(s):
    results = [''] * len(s)

    j = 0  # counter for when we find a word
    k = 0  # counter for our results array
    for i,x in enumerate(s):
        print(x)
        if x == ' ' or i == len(s)-1:
            while j < i+1:
                results[k] = s[j]
                j += 1
                k += 1
        
    return results;

def reverse_sentence_inplace(s: list):
    reverse_whole_string(s);
    reverse_individual_words(s);
    return s

def reverse_whole_string(s: list):
    i = 0
    j = len(s)-1
    while not i >= j:
        s[i],s[j] = s[j],s[i]
        i += 1
        j -= 1
    return s

def reverse_individual_words(s: list):
    i = 0   # counter until next space -- corresponds to end of word
    j = 0   # counter that marks left most spot of word
    
    while i <= len(s)-1:
        if s[i]==' ' or i==len(s)-1:
            p = j
            k = i if i==len(s)-1 else i-1
            print("%s\t%d\t%d" % (s[j:i],p,k))
            while not p >= k:
                s[p],s[k] = s[k],s[p]
                p += 1
                k -= 1
            j = i+1
        i += 1
    
    return s
    


if __name__ == "__main__":
    print(reverse_sentence_inplace(list('practice makes perfect')))
