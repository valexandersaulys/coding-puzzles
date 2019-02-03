#! usr/bin/python
"""
Say you have an array for which the ith element is the price of a 
given stock on day i. 

Like last problem, but now you can buy and sell as many times as 
you would like. However, you can only hold onto one stock at a time
"""

def max_profit(prices = []):
    """prices is assumed to be an array
    """
    minPrice = 10000000
    priceSums = 0
    
    for price in prices:
        if price < minPrice:
            minPrice = price;
        diff = price - minPrice
        priceSums += diff
    return priceSums


if __name__ == "__main__":
    print(max_profit([1,3,1,1,5]))
