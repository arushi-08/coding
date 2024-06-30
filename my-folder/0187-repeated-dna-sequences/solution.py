class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        substr = []
        for i in range(len(s)):
            substr.append(s[i:i+10])
        
        hmap = Counter(substr)

        ans = set()
        for k in hmap:
            if hmap[k] > 1:
                ans.add(k)
        return list(ans)

