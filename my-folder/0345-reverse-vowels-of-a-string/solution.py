class Solution:
    def reverseVowels(self, s: str) -> str:
        
        slist = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U']
        st = 0
        ed = len(s)-1
        while st < ed:
            if slist[st] not in vowels:
                st += 1
            if slist[ed] not in vowels:
                ed -= 1
            if slist[st] in vowels and slist[ed] in vowels:
                slist[st], slist[ed] = slist[ed], slist[st]
                st += 1
                ed -= 1
        return "".join(slist)
            

