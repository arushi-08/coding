class Solution:
    def decodeString(self, s: str) -> str:

        result = []
        stack = []
        i = 0
        digit = 0
        curr_scope = []
        while i < len(s):
            while s[i].isdigit():
                digit = digit * 10 + int(s[i])
                i += 1
            
            if s[i] == '[':
                # new scope
                stack.append([digit, curr_scope])
                digit = 0
                curr_scope = []
                i += 1
            
            elif s[i] == ']':
                # curr scope ended
                old_digit, old_scope = stack.pop()
                add_str = old_digit * ''.join(curr_scope)
                old_scope.append(add_str)
                curr_scope = old_scope
                i += 1
            
            else:
                curr_scope.append(s[i])
                i += 1
        
        return ''.join(curr_scope)



