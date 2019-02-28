#! usr/bin/env python
"""
From <https://www.youtube.com/watch?v=IWvbPIYQPFM>

Find the largest/longest number of connected components and return
the corresponding marker value and length.
"""
import numpy as np

# This should return ('o',5)
matrix = np.asarray([
    ['x','x','l','m'],
    ['x','o','l','m'],
    ['o','o','p','l'],
    ['o','o','p','m'],
    ['o','o','p','m']
])

def find_longest_section(M):
    width = matrix.shape[0]
    height = matrix.shape[1]

    best_marker = ''
    best_ct = -1

    for x in range(width):
        for y in range(height):
            marker,ct = specialized_bfs((x,y),M,width,height)
            #print("%s: %d" % (marker,ct))
            if ct > best_ct:
                best_marker = marker
                best_ct = ct
    return (best_marker,best_ct)

def specialized_bfs(start,M,width,height):
    marker = M[start]
    ct = 0
    to_visit = [start]
    visited = {}   # python sets don't take tuples (in 3.6 anyway)
    while to_visit:
        space = to_visit.pop()
        # check if we're out of bounds
        if (space[0] >= width or space[0] < 0) \
            or (space[1] >= height or space[1] < 0):
            continue
        # check if we've been here before
        if space in visited:
            continue
        # if not, add to our list of visited notes and start looking
        visited[space] = 1
        if M[space] == marker:
            ct += 1
            #print("%r: %s, %r" % (space,marker,visited))
        # add adjacent pieces
        to_visit.append((space[0]-1,space[1]))
        to_visit.append((space[0],space[1]-1))
        to_visit.append((space[0]+1,space[1]))
        to_visit.append((space[0],space[1]+1))
    return (marker,ct)


if __name__ == "__main__":
    print(find_longest_section(matrix));
