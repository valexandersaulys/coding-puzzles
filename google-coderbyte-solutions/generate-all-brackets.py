#! usr/bin/python3
"""
Generate all balanced parenthesis combinations
"""
def generate_parens(n):
    if n == 0:
        return []
    # current string, how many parenthesis are left to be open, how many to close
    return generate_parens_helper('', n, 0);

def generate_parens_helper(curr, num_available, num_unclosed):
    if num_available == 0:
        return [curr + ')'*num_unclosed]
    elif num_unclosed == 0:  # no more unclosed parenthesises to close
        return generate_parens_helper(curr+'(',num_available-1, num_unclosed+1)
    # either we open another bracket... or close it
    return generate_parens_helper(curr+'(',num_available-1, num_unclosed+1) + \
        generate_parens_helper(curr+')',num_available, num_unclosed-1)


if __name__ == "__main__":
    print(generate_parens(1));
    print(generate_parens(2));
    print(generate_parens(3));    

    
    
    
