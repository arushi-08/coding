class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        res = self.decode_count(s, memo)
        return res
    
    def decode_count(self, s, memo):
        
        if s.startswith("0"): return 0
        
        if not s or len(s) == 1:
            return 1
        
        if s in memo: return memo[s]
        
        first = self.decode_count(s[1:], memo)
        second = 0
        if int(s[0:2]) <= 26:
            second = self.decode_count(s[2:], memo)
        
        memo[s] = first + second
        return memo[s]


