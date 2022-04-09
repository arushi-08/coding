class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = strs[0]
        a = strs[0]
        
        for s in strs[1:]:
            
            common = ""
            for i in range(min(len(a), len(s))):
                if a[i] == s[i]:
                    common += a[i]
                else:
                    break
            a = common
        
        return common
