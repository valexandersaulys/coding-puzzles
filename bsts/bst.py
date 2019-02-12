#! usr/bin/python3
"""
Implementation of a Binary Search Tree in Python
"""
class Node(object):

    def __init__(self, data):
        assert (type(data)==int) or (type(data)==float)
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "%r" % self.data

    def __contains__(self,data):
        if self.data == data:
            return True
        elif self.left and self.right:
            return (data in self.left) or (data in self.right)
        elif self.left:
            return data in self.left
        elif self.right:
            return data in self.right
        return False

    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data >= self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

        self._balance()

    def _balance(self):
        """balance the tree"""
        pass

    def delete(self, key):
        """ delete the node with the given key and return the 
        root node of the tree """

        if self.key == key:
            # found the node we need to delete

            if self.right and self.left: 
                # get the successor node and its parent 
                [psucc, succ] = self.right._findMin(self)

                # splice out the successor
                # (we need the parent to do this) 

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor

                succ.left = self.left
                succ.right = self.right

                return succ                

            else:
                # "easier" case
                if self.left:
                    return self.left    # promote the left subtree
                else:
                    return self.right   # promote the right subtree 
        else:
            if self.key > key:          # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                    # else the key is not in the tree 
                    
            else:                       # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)
                    
        return self

    def _find_min(self, parent=None):
        """ return the minimum node in the current tree and its parent """
        if parent == None:
            parent = self;
        
        if self.left:
            return self.left._find_min(self,parent)
        else:
            return (parent, self)
        
    def inorder_traversal(self):
        """ returns a list in preorder """
        results = []
        if self.left:
            results += self.left.inorder_traversal()
        results.append(self.data)
        if self.right:
            results += self.right.inorder_traversal()
        return results;

    def preorder_traversal(self):
        """ returns a list in order """
        results = [self.data]
        if self.left:
            results += self.left.preorder_traversal()
        if self.right:
            results += self.right.preorder_traversal()
        return results

    def postorder_traversal(self):
        """ returns a list in post order """
        results = []
        if self.left:
            results += self.left.postorder_traversal()
        if self.right:
            results += self.right.postorder_traversal()
        results.append(self.data)
        return results

    def kth_largest(self,k):
        """Takes O(n) time to traverse and O(1) to select the kth largest"""
        if k < 1:
            raise ValueError("%d must be >= 1" % k)
        return self.inorder_traversal()[-k]

    

if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    print("%s" % root.preorder_traversal());  
    print("%s" % root.inorder_traversal());
    print("%s" % root.postorder_traversal());

    # Kth Largest Element
    print("%s" % root.kth_largest(1))

    print(min(root));
    

    
