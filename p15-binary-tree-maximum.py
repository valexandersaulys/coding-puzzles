#! usr/bin/python3
"""
Given a binary tree, find the maximum path sum. 

The path may start and end at any node in the tree.


>>> Note: there solution didn't work at all hmm... 
"""
class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def get_max_root(n,maxAcrossRoot):
    if n == None:
        return 0
    left = get_max_root(n.left, maxAcrossRoot)
    right = get_max_root(n.right, maxAcrossRoot)
    cmax = n.data

    if left > 0:
        cmax += left
    if right > 0:
        cmax += right

    maxAcrossRoot = max(maxAcrossRoot, cmax)
    return max(n.data, max(n.data+left, n.data+right))

def find_maximum_path_sum(n = None, s = 0):
    if n == None:
        return s
    """
    Four possible sums to consider:
      - node only
      - left + node
      - right + node
      - left + node + right

    go for the maximum in greedy fashion
    """
    maxAcrossRoot = -1
    maxEndByRoot = get_max_root(n, maxAcrossRoot)
    return max(maxAcrossRoot, maxEndByRoot)
    
        
if __name__ == "__main__":
    n = Node(1)
    n.right = Node(3)
    n.left = Node(2)

    print(find_maximum_path_sum(n))

