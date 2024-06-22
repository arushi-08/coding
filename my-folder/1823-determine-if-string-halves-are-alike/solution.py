class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        first = s[:len(s)//2].lower()
        second = s[len(s)//2:].lower()
        vowels = ('a', 'e', 'i', 'o', 'u')
        vfirstcount = 0
        vsecondcount = 0
        for v in vowels:
            vfirstcount += first.count(v)
            vsecondcount += second.count(v)
        
        return vfirstcount == vsecondcount


