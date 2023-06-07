"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # do bfs get next element in same level and populate it
        if not root: return None
        queue = deque()
        queue.append((1,root))
        bfs = [(1,root)]
        while queue:
            currlevel, currnode = queue.popleft()
            # print('currlevel', currlevel)
            for i in range(currlevel):
                if currnode.left:
                    bfs.append((currlevel+1, currnode.left))
                    queue.append((currlevel+1, currnode.left))
                if currnode.right:
                    bfs.append((currlevel+1, currnode.right))
                    queue.append((currlevel+1, currnode.right))
                break
            # print('queue', queue)
        for i in range(len(bfs)-1):
            if bfs[i][0] == bfs[i+1][0]:
                bfs[i][1].next = bfs[i+1][1]        
        return root


