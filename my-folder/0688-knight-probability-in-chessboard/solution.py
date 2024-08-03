class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # positions on board / positions anywhere
        if not k:
            return 1
        
        visited = {}
        return self.helper(n, k, row, column, visited)
    
    def helper(self, n, k, row, col, visited):

        if row < 0 or col < 0 or row >= n or col >= n:
            return 0

        if not k:
            return 1
        
        if (k, row, col) in visited:
            return visited[(k, row, col)]

        i = [-2,-1,1,2,2,1,-1,-2]
        j = [1,2,2,1,-1,-2,-2,-1]

        count = 0

        for x,y in zip(i, j):
            if row+x >= 0 and col+y >= 0 and row+x < n and col+y < n:
                count += self.helper(n, k-1, row+x, col+y, visited) / 8

        visited[(k, row, col)] = count
        return count
