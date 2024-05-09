"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque, defaultdict
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: return

        visited = {}
        
        copynode = self.helper(node, visited)

        return copynode
        
    def helper(self, node, visited):

        queue = deque()
        copynode = Node(node.val)
        queue.append(node)
        visited[node] = copynode
        while queue:
            og = queue.popleft()
            for neigh in og.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val)
                    queue.append(neigh)
                visited[og].neighbors.append(visited[neigh])
        
        return visited[node]

