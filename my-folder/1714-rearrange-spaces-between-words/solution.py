class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        if not text: return ""
        
        whitespace = 0
        for i in text:
            if ord(i) == 32: whitespace += 1
        
        if len(text.split())-1 == 0: 
            return "".join(text.split() + [" "]*(len(text) - len(text.split()[0])))
        inbetweenspace = whitespace//(len(text.split())-1)
        lastspace = whitespace%(len(text.split())-1)
        
        ans = ""
        for i, word in enumerate(text.split()):
            print(word)
            ans += word
            if i < len(text.split()) - 1:
                ans += "".join([" "]*inbetweenspace)
        
        return ans + "".join([" "]*lastspace)
