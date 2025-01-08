class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        if str2.startswith(str1) and str2.endswith(str1):
            return 1
        return 0

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                ans += self.isPrefixAndSuffix(words[i], words[j])

        return ans
