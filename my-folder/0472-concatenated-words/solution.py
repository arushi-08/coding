class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        words.sort(key=lambda x:len(x))
        words_set = set()
        res = []
        self.memo = {}

        for i, word in enumerate(words): #O(N)
            
            if self.wordbreak(word, words_set):
                res.append(word)
            words_set.add(word)
        return res
    
    def wordbreak(self, target_word, words_set):
        
        def helper(word):
            if word in words_set:
                return True
            if word in self.memo:
                return self.memo[word]
            
            for i in range(1, len(word)):
                if word[:i] in words_set and helper(word[i:]):
                    self.memo[word] = True
                    return True
                
            self.memo[word] = False
            return False
        
        return helper(target_word)

