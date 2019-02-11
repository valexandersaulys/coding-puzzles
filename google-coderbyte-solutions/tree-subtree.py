#! usr/bin/python
"""
Find if a tree is a valid subtree of another tree.

Soln: create in-order and pre-order reps of the trees and see if
they are contained within the larger tree.

O(n) to construct the trees)
O(n) to make the comparison
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def to_string(self):
        if self.left == None and self.right == None:
            return str(self.data)
        if self.left == None and self.right != None:
            return str(self.data) + "(,"+self.right.to_string()+")"
        if self.left != None and self.right == None:
            return str(self.data) + "(" + self.left.to_string()+",)"
        return str(self.data)+"("+self.left.to_string()+","+self.right.to_string()+")"
        

def subtree_in_tree(t1,t2):
    return (t2.to_string() in t1.to_string()) or (t1.to_string() in t2.to_string())

if __name__ == "__main__":
    # left tree
    root = Node(10)
    n1 = Node(4)
    n2 = Node(6)
    n3 = Node(30)
    
    # setup children
    n1.right = n3
    root.left = n1
    root.right = n2
    
    # right tree
    root_r = Node(26)
    n1_r = Node(10)
    n2_r = Node(3)
    n3_r = Node(4)
    n4_r = Node(6)
    n5_r = Node(3)
    n6_r = Node(30)
    
    # setup children
    n3_r.right = n6_r
    n1_r.left = n3_r
    n1_r.right = n4_r
    n2_r.right = n5_r
    root_r.left = n1_r
    root_r.right = n2_r

    print(subtree_in_tree(root_r,root))
    
