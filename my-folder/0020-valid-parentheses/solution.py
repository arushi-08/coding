
class Solution:
    def isValid(self, s: str) -> bool:
        
        
#         use stack -> list
        dict1 = {')':'(', '}':'{', ']': '['}
        stack = []
        for i in s:
            # s = "()[]{}"
            if i in dict1:
                if not stack:
                    return False
                print(1,i)
                if dict1[i] in stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(i)
            
        if stack:
            return False
        return True
        
        
