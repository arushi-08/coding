class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        stack = []
        primitives = []
        temp = ''
        ans = ''
        opencount = 0
        closecount = 0
        for char in s:
            temp += char
            if char == '(':
                opencount += 1
            else:
                closecount += 1
            if opencount == closecount:
                ans += temp[1:-1]
                temp = ''
        
        return ans


