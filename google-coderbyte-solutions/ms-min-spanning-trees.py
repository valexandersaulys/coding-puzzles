#! usr/bin/python3
"""
Find the minimum spanning tree (MST) that connects all the vertices in the 
graph while minimizing the total edge weights.


Solution
--------

We'll use Prim's algorithm. this is a classic greedy algorithm. 

(1) Create an empty structure M (adj matrix or binary tree) which 
    will be the MST
(2) Choose a random vertex v from the graph
(3) Add the edges taht are connected to v into some data structure E
(4) Find the edge in E with the minimum weight, and add this edge to M. 
    Now, make v equal to the other vertex in the edge and repeat from 
    step 3. 


https://coderbyte.com/algorithm/find-minimum-spanning-tree-using-prims-algorithm
"""
graph = {
    'a': [('b',2),('c',3)],
    'b': [('a',2),('c',5),('d',3),('e',4)],
    'c': [('a',3),('b',5),('e',4)],
    'd': [('b',3),('e',2),('f',3)],
    'e': [('b',4),('c',4),('d',2),('f',5)],
    'f': [('d',3),('e',5)]
}

def prims(G):
    edges = []
    collected_vertices = ['a']
    for k in G.keys():
        minEdge = (None,float('inf'))  # vertex,distance
        for v,e in G[k]:
            if (e < minEdge[1]) and (v==minEdge[0]):
                
        

if __name__ == "__main__":
    print(find_mst(graph))
