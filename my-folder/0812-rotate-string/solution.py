class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): return False

        
        P = 113
        MOD = 10**9 + 7
        Pinv = pow(P, MOD-2, MOD)

        hb = 0
        power = 1
        for x in goal:
            code = ord(x) - ord('a') + 1
            hb = (hb + power * code) % MOD
            power = power * P % MOD

        ha = 0
        power = 1
        for x in s:
            code = ord(x) - ord('a') + 1
            ha = (ha + power * code) % MOD
            power = power * P % MOD
        
        if ha == hb and s == goal:
            return True
        
        for i,x in enumerate(s):
            code = ord(x) - ord('a') + 1
            ha += power * code
            ha -= code
            ha *= Pinv
            ha %= MOD
            if ha == hb and s[i+1:] + s[:i+1] == goal:
                return True
        
        return False

