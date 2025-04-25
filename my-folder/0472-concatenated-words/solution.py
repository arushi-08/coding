class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        """
        return - [concat words]
        
        given a word, check if it can be broken

        """


        wordsset = set()
        words = sorted(words, key=lambda x:len(x))

        def can_break(word, idx):
            if idx == len(word):
                return True
            
            if idx in memo:
                return memo[idx]

            for i in range(1, len(word[idx:])):
                if (
                    ''.join(word[idx:idx+i]) in wordsset and can_break(word, idx+i)
                ):
                    memo[idx] = True
                    return True

            memo[idx] = ''.join(word[idx:]) in wordsset and idx > 0
            return memo[idx]

        results = []
        for i, word in enumerate(words):
            if i > 0:
                memo = {}
                if can_break(list(word), 0):
                    results.append(word)
            wordsset.add(word)
        
        return results

