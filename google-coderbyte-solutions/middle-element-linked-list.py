#! usr/bin/python3
"""
Find the middle element of a linked list
"""
class Node(object):

    def __init__(self, data, next=None):
        self.data = data;
        self.next = next;


def find_middle_element(node):
    if node == None:
        return;

    speed1 = node;
    speed2 = node;

    while speed2.next:
        speed1 = speed1.next;
        speed2 = speed2.next.next;

    return speed1
    
        
if __name__ == "__main__":

    l = [1,2,5,6,7,8]  
    head_node = Node(data=0)   # [0 1 2  >5<  6 7 8]
    node = head_node
    for i in l:
        new_node = Node(data=i)
        node.next = new_node
        node = new_node

    print(find_middle_element(head_node).data)
    
