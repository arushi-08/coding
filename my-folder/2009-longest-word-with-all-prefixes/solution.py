class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        wordsset = set(words)
        words = sorted(words, reverse=True, key=len)
        maxlength = 0
        answers = []
        for word in words:
            if len(word) < maxlength:
                break

            prefix_count = 0
            for i in range(len(word)):
                if word[:i+1] in wordsset:
                    prefix_count += 1
                else:
                    break
            if prefix_count == len(word):
                maxlength = max(maxlength, prefix_count)
                answers.append(word)

        if not answers:
            return ''
            
        return sorted(answers)[0]
