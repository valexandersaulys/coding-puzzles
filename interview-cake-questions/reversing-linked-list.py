#! usr/bin/python3
class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    start = head
    
    prev = None
    current = head
    _next = head.next

    while current:
        current.next = prev
        
        prev = current
        current = _next
        
        if _next:
            _next = _next.next

    return(prev)  # this was counter-intuitive, I originally did head


def print_linked_list(node):
    s = ''
    while node:
        s += str(node.data) + ' '
        node = node.next
    print(s);

        
if __name__ == "__main__":
    node = Node(1)
    start_node = node
    for i in range(2,6):
        node.next = Node(i)
        node = node.next

    print_linked_list(start_node)
    print_linked_list(reverse_linked_list(start_node))


    
