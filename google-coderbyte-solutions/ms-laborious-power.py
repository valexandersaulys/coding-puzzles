#! usr/bin/python3
"""
Implement pow(a,b) without multiplication or division
"""

def pow(a,b):  # 2,2 = 4
    result = a;
    for _ in range(1,b):  # loop over exponent => remember that we want to miss this if b is 1!
        added = 0
        for _ in range(a):  # do multiplication
            added += result   # will add this twice
        result = added
    return result


if __name__ == "__main__":
    print(pow(3,4));
