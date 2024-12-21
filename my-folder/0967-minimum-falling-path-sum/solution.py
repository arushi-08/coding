class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        # return min sum of any falling path through matrix

        # below or diag left/right

        m = len(matrix)
        n = len(matrix[0])

        prev = [float('inf')] * n

        for i in range(m):
            curr = [float('inf')] * n

            for j in range(n):
                if i == 0:
                    curr[j] = matrix[i][j]
                elif j == 0:
                    curr[j] = min(prev[j], prev[j+1]) + matrix[i][j]
                elif j == n-1:
                    curr[j] = min(prev[j-1], prev[j]) + matrix[i][j]
                else:
                    curr[j] = min(prev[j-1], prev[j], prev[j+1]) + matrix[i][j]
            
            prev = curr
        return min(prev)
