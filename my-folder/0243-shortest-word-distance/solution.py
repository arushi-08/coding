class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        w1idx = -1
        w2idx = -1
        mindist = float('inf')
        for i, wd in enumerate(wordsDict):
            if wd == word1:
                w1idx = i
                if w2idx != -1:
                    mindist = min(mindist, w1idx - w2idx)
                    w2idx = -1
    
            elif wd == word2:
                w2idx = i
                if w1idx != -1:
                    mindist = min(mindist, w2idx - w1idx) 
                    w1idx = -1
            
        return mindist
