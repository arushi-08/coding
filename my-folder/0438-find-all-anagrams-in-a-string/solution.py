from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            # s = cbaebabacd , p = abc o/p = [0, 6]
        if len(s) < len(p): return []
        i = 0
        j = len(p) - 1
        freq_p = Counter(p)
        answer = []
        while j < len(s):
            window = Counter(s[i:j + 1])
            if window == freq_p:
                answer.append(i)
            i += 1
            j += 1
        return answer    
            

