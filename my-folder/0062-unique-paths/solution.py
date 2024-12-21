class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1: return 1

        # dp = [[0] * n for _ in range(m)]
        prev_m = [0]*n
        for i in range(m):
            prev_n = [0]*n
            for j in range(n):
                if i < 0 and j < 0:
                    prev_n[j] = 0
                elif i == 0 and j == 0:
                    prev_n[j] = 1
                else:
                    prev_n[j] = prev_m[j] + prev_n[j-1]
            prev_m = prev_n

        return prev_m[-1]

