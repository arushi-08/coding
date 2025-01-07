class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
    
        sentence = ' '.join(words)
        ans = []
        for word in words:
            if sentence.count(word) > 1:
                ans.append(word)
        
        return ans
