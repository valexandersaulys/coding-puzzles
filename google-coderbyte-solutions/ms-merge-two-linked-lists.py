#! usr/bin/python3
"""
Merge two sorted linked lists
"""
class Node(object):

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def merge_llists(head1,head2):
    new_head = Node(None)
    pointer = new_head
    
    while head1 != None and head2 != None:
        if head1.data <= head2.data:
            pointer.next = head1
            head1 = head1.next
        else:
            pointer.next = head2
            head2 = head2.next

        pointer = pointer.next

    if head1 == None:
        pointer.next = head2
    elif head2 == None:
        pointer.next = head1
        
    return new_head.next
        


def print_llists(head):
    s = ''
    while head:
        s += str(head.data) + ' ';
        head = head.next
    return s;

if __name__ == "__main__":
    l = [6,9]
    head_node1 = Node(data=5)
    node = head_node1
    for i in l:
        new_node = Node(data=i)
        node.next = new_node
        node = new_node

    l = [3,10]
    head_node2 = Node(data=1)  
    node = head_node2
    for i in l:
        new_node = Node(data=i)
        node.next = new_node
        node = new_node

    print(print_llists(head_node1))
    print(print_llists(merge_llists(head_node1,head_node2)))
