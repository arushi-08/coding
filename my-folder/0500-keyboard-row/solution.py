class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"

        ans = []
        for word in words:
            w = word.lower()
            if set(w)-set(l1)==set() or set(w)-set(l2)==set() or set(w)-set(l3)==set():
                ans.append(word)
        
        return ans
        

