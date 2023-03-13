"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        queue = deque()
        queue.append(node)
        visited[node] = Node(node.val)
        while len(queue):
            curr = queue.popleft()
            for n in curr.neighbors:
                if n not in visited:
                    queue.append(n)
                    visited[n] = Node(n.val)
                visited[curr].neighbors.append(visited[n])
        
        return visited[node]
