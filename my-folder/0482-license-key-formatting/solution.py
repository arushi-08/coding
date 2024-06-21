class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
    
        # convert 1 to n groups to k length
        # uppercase chars

        n = len(s)
        count = 0
        ans = ['']
        for i in range(n-1, -1, -1):
            if s[i] != '-':
                ans += s[i]
                count += 1
                if count == k:
                    count = 0
                    ans += '-'
        
        if ans and ans[-1] == '-':
            ans = ans[:-1]
        ans = ans[::-1]
        result = ''.join(ans).upper()
        return result

