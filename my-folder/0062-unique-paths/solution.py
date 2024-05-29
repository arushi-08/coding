class Solution:

    def __init__(self):
        self.memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        

        # move down or right
        if m == 1 or n == 1:
            return 1
        
        if m == 2 and n == 2:
            return 2
        
        if (m,n) in self.memo:
            return self.memo[(m,n)]

        self.memo[(m,n)] =  self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.memo[(m,n)]
