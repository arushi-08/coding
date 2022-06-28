from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        i = 0
        j = 0
        hmap = {}
        ans = []
        p_freq = Counter(p)
        # print(p_freq)
        window = Counter(s[j:len(p)+j])
        while j < len(s):
            # print("window", window)
            if window == p_freq:
                ans.append(j)
                
            j += 1
            if j + len(p) - 1 >= len(s):
                break
            window[s[i]] -= 1
            window[s[j + len(p) - 1]] = window.get(s[j + len(p) - 1], 0) + 1
            i += 1
        return ans
