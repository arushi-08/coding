"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # if current grid has same value = set isleaf = true
        # val = val of grid

        # else isleaf = False, val can be any value
        
        if not grid: return 
        r = len(grid)
        c = len(grid[0])
        val = grid[0][0]
        isLeaf = True
        for i in range(r):
            for j in range(c):
                if grid[i][j] != val:
                    isLeaf = False
                    break
            if not isLeaf:
                break
        
        topLeft = None
        topRight = None
        bottomLeft = None
        bottomRight = None
        if not isLeaf:
            r_half, c_half = r//2, c//2
            topLeft = self.construct([grid[i][:c_half] for i in range(r_half)])
            topRight = self.construct([grid[i][c_half:] for i in range(r_half)])
            bottomLeft = self.construct([grid[i][:c_half] for i in range(r_half, len(grid))])
            bottomRight = self.construct([grid[i][c_half:] for i in range(r_half, len(grid))])

        curr = Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        
        return curr

