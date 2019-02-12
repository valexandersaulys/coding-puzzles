#! usr/bin/python
"""
A minimum spanning tree of a weighted,directed graph that minimizes
the summed weight of the path that connects all nodes. 

Prim's Algorithm is one of these. You will need a binary heap to
implement this. 

Priority Queue (Min Binary Heap) supports:

  - extract_min()    -> heapq.heappop(heap=[])
  - add(value)       -> heapq.heappush(heap=[])
  - contains(value)  -> value in heap
  - decrease()       -> 

It supports storage of values such that the minimum value is always at
top. 

You can use heapq library in python to implement this =>
https://docs.python.org/3.7/library/heapq.html 
"""
import sys # Library for INT_MAX 
  
class Graph(): 
  
    def __init__(self, vertices: list):
        # note down all the vertices in list form
        self.V = vertices
        # generate empty adjacency matrix
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)] 
  
    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, parent): 
        print("Edge \tWeight")
        for i in range(1,self.V): 
            print(parent[i],"-",i,"\t",self.graph[i][ parent[i] ] )
  
    def min_key(self, key, mstSet):
        """
        A utility function to find the vertex with  
        minimum distance value, from the set of vertices  
        not yet included in shortest path tree 
        """
  
        # Initilaize min value 
        min = sys.maxsize

        # iterate over all the vertices around
        for v in range(self.V):
            # if we find one that is smaller than what exists in our current set...
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    def prim_mst(self): 
        """
        Function to construct and print MST for a graph  
        represented using adjacency matrix representation 
        """
        # Key values used to pick minimum weight edge in cut 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V # Array to store constructed MST 

        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1 # First node is always the root of 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.min_key(key, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent) 


if __name__ == "__main__":
    g = Graph(5) 
    g.graph = [ [0, 2, 0, 6, 0], 
                [2, 0, 3, 8, 5], 
                [0, 3, 0, 0, 7], 
                [6, 8, 0, 0, 9], 
                [0, 5, 7, 9, 0]] 
  
    g.primMST(); 
    


