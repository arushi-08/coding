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
        if not node: return node
        visited = []
        queue = deque()
        newnode = Node(node.val)
        queue.append((node, newnode))
        visited = {}
        while len(queue):
            curr, currnew = queue.popleft()
            visited[curr] = currnew
            for n in curr.neighbors:
                if n not in visited:
                    nnew = Node(n.val)
                    visited[n] = nnew
                    currnew.neighbors.append(nnew)
                    queue.append((n, nnew))
                else:
                    currnew.neighbors.append(visited[n])

        # for n in newnode.neighbors:
        #     print('n neighbors: ',n.val)
        #     for i in n.neighbors:
        #         print(i.val)

        return newnode

