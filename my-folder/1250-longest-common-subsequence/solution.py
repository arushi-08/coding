class Solution:
    def __init__(self):
        self.memo = {}
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if not text1 or not text2: return 0
        if text1 == text2: return len(text1)
        
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
        
        # for i in range(len(text1)):
        #     for j in range(len(text2)):
        #         if dp[i][j] == 1:
                    
                
        
#         if (text1, text2) in self.memo:
#             return self.memo[(text1, text2)]
        
#         if text1[0] == text2[0]: 
#             self.memo[(text1, text2)] = self.longestCommonSubsequence(text1[1:], text2[1:]) + 1
#         else:
#             self.memo[(text1, text2)] = max(self.longestCommonSubsequence(text1, text2[1:]),
#                       self.longestCommonSubsequence(text1[1:], text2))
        
#         return self.memo[(text1, text2)]
