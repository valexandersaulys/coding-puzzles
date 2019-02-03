#! usr/bin/python
"""
Say you have an array for which the ith element is the price of a 
given stock on day i. 

If you were only permitted to complete at most one transaction (buy
and sell one share of stock), design an algorithm to find the 
maximum profit. 

>>> Not sure what the difficult in this was?
"""

def max_profit(prices = []):
    """prices is assumed to be an array
    """
    minPrice = 10000000
    _max = 0
    
    for price in prices:
        if price < minPrice:
            minPrice = price;
        diff = price - minPrice
        if _max < diff:
            _max = diff
    return _max


if __name__ == "__main__":
    print(max_profit([1,1,1,1,5]))
