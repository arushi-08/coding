class Solution:
    def __init__(self):
        self.memo = {}
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s: return True
        
        if s in wordDict: return True
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                
        return dp[-1]
                
            
        
#         if s in self.memo: return self.memo[s]
        
#         ans = True
#         for word in wordDict:
#             if word == s[:len(word)]:
#                 self.memo[s] = self.wordBreak(s[len(word):], wordDict)
#                 if self.memo[s]:
#                     return self.memo[s]
                
#         return False
