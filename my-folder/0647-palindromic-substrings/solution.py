class Solution:
    def countSubstrings(self, s: str) -> int:
        
        return self.helper(s)
    
    def helper(self ,s):
        if not s: return 0
        if len(s) == 1: return 1
        
        dp = [[0]*len(s) for _ in range(len(s))]
        

        for i in range(len(s)):
            for j in range(len(s)):
                
                if i > j:
                    continue
                    
                if i == j:
                    dp[i][j] = 1
                    
                elif (i == j + 1 or j == i + 1) and s[i] == s[j]:
                    dp[i][j] = 1
        # print(dp)
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)):
                if i > j:
                    continue
                # if i == 0 and j == 4:
                #     print(i + 1 < len(s) ,  j - 1 >= 0 ,  dp[i+1][j-1] != 0 , s[i] == s[j])
                if i + 1 < len(s) and j - 1 >= 0 and dp[i+1][j-1] != 0 and s[i] == s[j]:
                    dp[i][j] = 1
        # print(dp)
        return sum(map(sum, dp))
        
