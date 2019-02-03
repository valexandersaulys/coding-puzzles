#! usr/bin/python3
"""
Given a binary tree, return the _preorder_ traversal of its node's
values.

Can you do this iteratively?


>>> Note: I believe this grabs the node's value, then left, then right
"""
class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(n = Node(None)):
    if n == None:
        return '';
    
    s = str(str(n.data) + " "
            + preorder_traversal(n.left)
            + preorder_traversal(n.right))
            
    return s

def preorder_traversal_iterative(n = Node(None)):
    stack = []   # stack is LIFO
    results = []
    """
    python has queues in queue.Queue, which has q.put and q.get methods
    """
    stack.append(None)
    top = n
    while top != None:
        results.append(top.data)
        if top.right != None:
            stack.append(top.right)
        if top.left != None:
            stack.append(top.left)
        top = stack.pop()
    return ' '.join(str(i) for i in results)
    
    
    

if __name__ == "__main__":
    n = Node(1)
    n.right = Node(2)
    n.right.left = Node(3)

    print(preorder_traversal(n))
    print(preorder_traversal_iterative(n))

