class Solution:
    def decodeString(self, s: str) -> str:
        
        # iterate on s
        # store elements in stack
        # when we arrive on close bracket
        # pop out elements acc to count given outside bracket

        stack = []
        number = ''
        enter_stack = False

        for i in range(len(s)):
            if s[i].isdigit():
                number += s[i]
            elif s[i] == '[':
                stack.append(number)
                stack.append(s[i])
                number = ''
            elif s[i] == ']':
                string_element = ''
                while stack[-1] != '[':
                    string_element = stack.pop() + string_element
                if stack[-1] == '[':
                    stack.pop()
                    old_num = stack.pop()
                stack.append(int(old_num) * string_element)

            else: # s[i] is char
                stack.append(s[i])

        ans = ''
        while stack:
            ans = stack.pop() + ans
        return ans
