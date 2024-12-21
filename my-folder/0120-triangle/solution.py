class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # index i on current row -> move to index i or index i + 1
        # min path sum from top to bottom
        m = len(triangle)
        n = max([len(triangle[i]) for i in range(m)])

        prev = [float('inf')] * len(triangle[0])

        for i in range(m):
            n = len(triangle[i])
            curr = [float('inf')] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = triangle[i][j]
                elif j == 0:
                    curr[j] = prev[j] + triangle[i][j]   
                elif j == n-1:
                    curr[j] = prev[j-1] + triangle[i][j]               
                else:
                    curr[j] = min(prev[j], prev[j-1]) + triangle[i][j]               
            prev = curr

        return min(prev)

