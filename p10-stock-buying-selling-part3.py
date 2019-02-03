#! usr/bin/python
"""
Say you have an array for which the ith element is the price of a 
given stock on day i. 

Find the maximum profit given that you can complete at most _two_
transactions.

>>> Note: this is different than in the book, but I actually think its 
better at O(n) time complexity. 
"""

def max_profit(prices = []):
    """prices is assumed to be an array
    """
    minPrice = 10000000
    _max1 = 0
    _max2 = 0
    
    for price in prices:
        if price < minPrice:
            minPrice = price
        diff = price - minPrice
        if _max1 < diff:
            _max2 = _max1
            _max1 = diff
        elif _max2 < diff:
            _max2 = diff
            
    return _max1 + _max2


if __name__ == "__main__":
    print(max_profit([1,3,1,1,5,1,6]))
