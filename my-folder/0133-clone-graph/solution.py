"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        hashmap{ curr_node: clone_node }
        """
        if not node: return 
        # clone graph
        clone_map = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for neigh in curr.neighbors:
                if neigh not in clone_map:
                    clone_map[neigh] = Node(neigh.val)
                    queue.append(neigh)
                clone_map[curr].neighbors.append( clone_map[neigh] )
        
        return clone_map[node]


