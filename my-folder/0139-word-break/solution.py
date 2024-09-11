class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if s == '':
            return True
        
        if s in self.memo:
            return self.memo[s]

        for word in wordDict:
            if s == word:
                return True
            if s.startswith(word):
                if self.wordBreak(s[len(word):], wordDict):
                    self.memo[s] = True
                    return True
                    
        self.memo[s] = False
        return False



