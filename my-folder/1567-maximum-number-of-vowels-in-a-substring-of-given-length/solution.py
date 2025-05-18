class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window

        vowels = set('aeiou')

        if k >= len(s):
            result = 0
            for v in vowels:
                result += s.count(v)
            return result

        st = 0
        ed = 0
        maxvowelresult = 0
        currvowel = 0
        

        while ed < len(s):
            if ed - st + 1 > k:
                if s[st] in vowels:
                    maxvowelresult = max(maxvowelresult, currvowel)
                    currvowel -= 1
                st += 1
            
            if s[ed] in vowels:
                currvowel += 1

            ed += 1

        return max(maxvowelresult, currvowel)
        



