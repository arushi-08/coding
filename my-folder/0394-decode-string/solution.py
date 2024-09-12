class Solution:
    def decodeString(self, s: str) -> str:
        
        # use stack to store substrings
        # store digits & substrings in stack
        # when i=']':
        #       pop stack -> substring
        #       substring * digits -> stack
        # in the end read from stack


        stack = []
        i = 0

        while i < len(s):
            if s[i] == ']':
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                if stack[-1] == '[':
                    stack.pop()
                digit = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(substring * int(digit))
            else:
                stack.append(s[i])
            i += 1

        ans = ''
        while stack:
            ans = stack.pop() + ans
        
        return ans
