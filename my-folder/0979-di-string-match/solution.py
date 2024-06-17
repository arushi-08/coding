class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        # if i encountered put smaller
        # if d encountered put bigger
        ans = [0] * (len(s)+1)
        st = 0
        ed = len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                ans[i] = st
                st += 1
            else:
                ans[i] = ed
                ed -= 1
        ans[len(s)] = st
        return ans

