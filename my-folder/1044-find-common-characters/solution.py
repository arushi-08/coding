class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        

        q = Counter(words[0])
        for p in map(Counter, words[1:]):
            temp = {}
            for ch in p:
                temp[ch] = min(p[ch], q[ch])
            q = Counter(temp)
        
        return q.elements()

