class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        for loop on s
        see if s[:i] in wordDict
        if it is, add a break point
        # see if s[breakpoint: i] in wordDict
        """

        wordset = set(wordDict)
        st = 0
        self.memo = {}
        
        def helper(word):
            if word in self.memo:
                return self.memo[word]
            if word in wordset:
                return True

            st = 0
            for i in range(1, len(word)):
                if word[:i] in wordset and helper(word[i:]):
                    self.memo[word] = True
                    return True

            self.memo[word] = False
            return False

        return helper(s)

        # greedily putting a breakpoint
        # we need to check if s[st:i] or another value
        # a->a->a->a->a->a->a

