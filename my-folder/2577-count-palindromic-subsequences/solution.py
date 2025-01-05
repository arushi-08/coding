class Solution:
    def countPalindromes(self, s: str) -> int:
        
        mod = 10**9+7
        n = len(s)
        ans = 0

        pre = [[[0]*10 for _ in range(10)] for _ in range(n)]
        cnts = [0] * 10

        for i in range(n):
            c = ord(s[i]) - ord('0')
            if i:
                for j in range(10):
                    for k in range(10):
                        pre[i][j][k] = pre[i-1][j][k]
                        if k == c:
                            pre[i][j][k] += cnts[j]
            cnts[c] += 1
        

        suff = [[[0]*10 for _ in range(10)] for _ in range(n)]
        cnts = [0] * 10

        for i in range(n-1,-1,-1):
            c = ord(s[i]) - ord('0')
            if i < n-1:
                for j in range(10):
                    for k in range(10):
                        suff[i][j][k] = suff[i+1][j][k]
                        if k == c:
                            suff[i][j][k] += cnts[j]
            cnts[c] += 1
        ans = 0
        for i in range(2, n-2):
            for j in range(10):
                for k in range(10):
                    ans += pre[i-1][j][k] * suff[i+1][j][k]
        
        return ans % mod

