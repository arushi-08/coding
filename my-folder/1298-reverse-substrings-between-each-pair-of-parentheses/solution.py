class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        for char in s:
            if char == ')':
                substr = ''
                while stack[-1] != '(':
                    substr = stack.pop() + substr
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(substr[::-1])
                    
            else:
                stack.append(char)
        
        return ''.join(stack)
