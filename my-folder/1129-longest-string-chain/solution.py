class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        #LIS with 1 change: comparing 2 words
        words.sort(key=len)
        n = len(words)
        dp = [1] * (n+1)
        visited = {}
        
        for i in range(1, n):
            for j in range(i):
                if (len(words[i]) == len(words[j]) + 1
                and self.compare_optim(words[i], words[j])):
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
    
    def compare_optim(self, word1, word2):
        
        bigger_word = ""
        smaller_word = ""
        if len(word1) > len(word2):
            bigger_word = word1
            smaller_word = word2
        else:
            bigger_word = word2
            smaller_word = word1
        
        for w in range(len(bigger_word)):
            if bigger_word[:w] + bigger_word[w+1:] == smaller_word:
                return True
        return False
            
