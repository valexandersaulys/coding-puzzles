#! usr/bin/env python3
"""Max heaps would have the array's comparisons get replaced by their opposite"""

class MinHeap(object):

    def __init__(self,array):
        self.heap = self.build_heap(array)

    def build_heap(self,array):
        parent_node = (len(array)-1) // 2
        for node in reversed(range(parent_node)):
            self.sift_down(node, len(array)-1, array)
        return array

    def sift_up(self, current_node, heap):
        parent_node = (current_node - 1) // 2
        while current_node > 0 and heap[current_node] < heap[parent_node]:
            heap[current_node], heap[parent_node] = heap[parent_node], heap[current_node]
            curret_node = parent_node
            parent_node = (current_node - 1) // 2
        return heap

    def sift_down(self, current_node, last_node, heap):
        child_node_one = current_node*2 + 1
        while child_node_one <= last_node:
            # get the second child
            child_node_two = current_node*2 + 2 if current_node*2+2 <= last_node else -1

            # determine which is smaller to swap
            if child_node_two != -1 and heap[child_node_two] < heap[child_node_one]:
                swap_node = child_node_two
            else:
                swap_node = child_node_one

            # swap them if our current_node is greater than smaller of children nodes
            if heap[current_node] > heap[swap_node]:
                heap[current_node], heap[swap_node] = heap[swap_node], heap[current_node]
                
                # update values and continue the loop
                current_node = swap_node
                child_node_one = swap_node*2 + 1
            else:
                # if we're good so far, we'll break out of our loop
                break
            
        return heap

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        smallest_value = self.heap.pop()
        self.heap = self.sift_down(0, len(self.heap)-1, self.heap)
        return smallest_value

    def peak(self):
        return self.heap[0]

    def insert(self,value):
        self.heap.append(value)
        self.heap = self.sift_up(len(self.heap)-1, self.heap)
        return True


if __name__ == "__main__":
    heap = MinHeap([6,5,4,3,2,1,106,239,1057123])
    #print(heap.heap)

    print(heap.remove())
    #print(heap.heap)
    
    heap.insert(41)
    #print(heap.heap)

    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
    heap.insert(1)
    
    print(heap.peak())
    heap.heap

    print(heap.remove())

    # print the final heap
    print(heap.heap)

