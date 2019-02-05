#! usr/bin/python3
"""
From https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/ 
=> I didn't like the explanation in the book

graph = {
  # node: [list of nodes it connects to]
  1: [1,2,3,4]
}
"""

def depth_first_search(graph,start):
    """
    graph is our graph, start is our starting 
    node, target is our target node.
    """
    # we add our starting node as the first place to visit
    stack = [start]
    # we initialize our visited set to be nothing
    visited = set()
    # while we have a stack of things
    while stack:
        # we pop off (FIFO for a stack) aa vertex to visit
        vertex = stack.pop()
        # if our vertex has not been visited...
        if vertex not in visited:
            # we visit it!
            visited.add(vertex)
            # and add in all the nodes it connected to
            A = list(set(graph[vertex]) - visited)
            stack.extend(A)
    return visited

def recursive_dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in set(graph[start]) - visited:
        recursive_dfs(graph,next,visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start,[start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path  + [next]
            else:
                stack.append((next, path+[next]))

def bfs(graph, start):
    visited,queue = set(), [start]
    # same as DFS but with a _queue_ instead of a stackx
    while queue:
        # equivelant to grabbing the first value from our queue for LIFO implementation
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return vertex

def bfs_paths(graph,start,goal):
    queue = [(start,[start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                # reveal our path if its relevant
                yield path + [next]
            else:
                # for each node, we add the existing path
                queue.append((next,  
                              path+[next]))


if __name__ == "__main__":
    graph = {
        'A': ['E','D'],
        'D': ['A','B'],
        'B': ['D'],
        'E': ['A'],
        'C': ['F'],
        'F': ['C']
    }
    print(depth_first_search(graph,'A'))
    print(depth_first_search(graph,'C'))

    print(recursive_dfs(graph,'A'))
    print(recursive_dfs(graph,'C'))

    print(list(dfs_paths(graph,'A','B')))

    
