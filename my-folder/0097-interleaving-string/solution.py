class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(s1ptr, s2ptr, s3ptr):
            nonlocal memo

            if (s1ptr, s2ptr, s3ptr) in memo:
                return memo[(s1ptr, s2ptr, s3ptr)]

            if s1ptr == len(s1) and s2ptr == len(s2) and s3ptr == len(s3):
                memo[(s1ptr, s2ptr, s3ptr)] = True
                return True
            
            if s3ptr == len(s3):
                memo[(s1ptr, s2ptr, s3ptr)] = False
                return False

            if s1ptr < len(s1) and s1[s1ptr] == s3[s3ptr]:
                if dfs(s1ptr+1, s2ptr, s3ptr+1):
                    return True
            
            if s2ptr < len(s2) and s2[s2ptr] == s3[s3ptr]:
                if dfs(s1ptr, s2ptr+1, s3ptr+1):
                    return True
            
            memo[(s1ptr, s2ptr, s3ptr)] = False
            return False
        
        return dfs(0,0,0)
