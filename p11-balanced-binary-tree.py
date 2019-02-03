#! usr/bin/python3
"""
Given a binary tree, determine if its height balanced.

A height balanced tree is defined as a binary tree where
the depth of two subtrees of every node never differs by
more than 1.
"""
class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def get_height(root = Node(None), level=0):
    if root == None:
        return level

    return max( get_height(root.left, level=level+1),
                get_height(root.right, level=level+1) )
    

def is_balanced(root = Node(None)):
    if root == None:
        return True
    
    left = get_height(root.left, level=0)
    right = get_height(root.right, level=0)

    if abs(left-right) > 1:
        return False
    else:
        return True
    
    

if __name__ == "__main__":

    # This is a balanced tree
    n = Node(3)
    n.left = Node(2)
    n.right = Node(5)
    n.right.left = Node(6)
    n.left.right = Node(7)
    print(is_balanced(n))
    
    # This is __not__ a balanced tree
    n = Node(3)
    n.left = Node(2)
    n.right = Node(5)
    n.right.right = Node(6)
    n.right.right.right = Node(7)
    print(is_balanced(n))
