#! usr/bin/python3
"""
Write a function that takes two strings as arguments, s & p,
and returns a boolean denoting whether s matches p.

p is a sequence of any number of the following:

ignore .* for now

does i equal the length of p?
  * we found a match! set match to True

  1. a-z :  standing for itself
     yes -> increment i
     no -> is the next a wild card? can I even check it?
       yes -> increment i
       no -> reset i to 0, j to k
  2.  .  : any character
     yes -> increment i
     no -> reset i to 0, j to k
  3.  *  : matches 0 _or more_ occurences of the previous character
     yes -> does the previous character match the current one?
     no -> increment i (can be zero after all)


"""
def regexp_parser(s,p):
    if '*.' in p:
        return True  # will pattern match anything
    
    i = 0  # counter for p
    j = 0  # counter for short end of potential match
    match = False

    for k,c in enumerate(s):
        #print("%d\t%d\t%d\t%s\t%s" % (i,j,k,c,p[i]))
            
        # base case
        if i >= len(p):
            match = True
            break;

        # a-z?
        elif p[i] != '.' and p[i] != '*':
            if c == p[i]:
                i += 1
                continue
            # what if next is a wild card? can I check?
            elif i+1 < len(p):
                if p[i+1] == '*':
                    i += 1
                    continue
            i,j = 0,k;

        # . ?
        elif '.' == p[i]:
            i += 1

        # * ?
        elif ('*' == p[i]):
            if p[i-1] == c:
                continue
            elif i+1 < len(p):
                if p[i+1] == c:
                    i += 2
            else:
                i += 1
                
        else:
            i,j = 0,k;

    return match


def regexp_parser_first_attempt(s,p):
    # p can't begin with *, only char or . -- begins with ., I
    # don't care.
    i = 0  # counter for p
    j = 0  # counter for short end of potential match
    result = False
    
    for k,c in enumerate(s):
        print("%d\t%d\t%d\t%s\t%s" % (i,j,k,c,p[i]))
        
        # base case: we hit the end of p, add to results
        if i == len(p):
            result = True
            i,j = 0, k

        # we have a wildcard, look back 1 if we can -- can be 0 though
        elif (p[i]=='*') and (i != 0):
            result = True
            if p[i-1] == c: 
                continue
            i,j = 0,k

        elif (p[i+1]=='*'):
            i += 1
            

        # skip over '.' characters or if they're equal or if our next character is a wild card
        elif (p[i]=='.') or (p[i]==c):
            i += 1
            
        # reset p counter, short end of match string matches k
        else:
            i,j = 0,k


    print("%d\t%d\t%d\t%s" % (i,j,k,c))
    
    if (i == len(p)):  # we had hit the end of p
        result = True
    elif (p[i]==c):
        result = True
    if i < len(p)-1:
        if (p[i+1]=='*'):
            result = True

    return result


if __name__ == "__main__":
    #print(regexp_parser(s='weeeeeee blank we',p='we*'))

    print(regexp_parser(s='wee weeeeee',
                        p='w*'))
