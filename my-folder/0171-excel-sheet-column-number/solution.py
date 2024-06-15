class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0
        for i in range(len(columnTitle)-1,-1,-1):
            ans += (ord(columnTitle[i]) - ord('A') + 1) * 26 ** (len(columnTitle)-1-i)

        
        return ans


