class Solution:
    def minimumTime(self, s: str) -> int:
        lpsum = [0]*len(s)
        lpsum[0] = int(s[0])
        for i in range(1, len(s)):
            if s[i] == '1':
                lpsum[i] = min(lpsum[i-1]+2, i+1)
            else:
                lpsum[i] = lpsum[i-1] 
        
        rpsum = [0]*len(s)
        rpsum[-1] = int(s[-1])
        for i in range(len(s)-2,-1,-1):
            if s[i] == '1':
                rpsum[i] = min(rpsum[i+1]+2, len(s)-i)
            else:
                rpsum[i] = rpsum[i+1] 
        ans = min(lpsum[-1], rpsum[0])
        for i in range(1, len(s)-1):
            ans = min(ans, lpsum[i] + rpsum[i+1])
        
        return ans 
