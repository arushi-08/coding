class Solution:
    def decodeString(self, s: str) -> str:
        
        i = 0
        digit=''
        stack = []
        curr_str = ''
        
        for i in range(len(s)):

            if s[i].isdigit():
                digit += s[i]

            elif s[i] == '[':
                stack.append(digit)
                stack.append(curr_str)
                digit = ''
                curr_str = ''

            elif s[i] == ']':
                prev_str = stack.pop()
                prev_num = stack.pop()

                curr_str = prev_str + curr_str * int(prev_num)
                
            else:
                curr_str += s[i]

        while stack:
            curr_str = stack.pop() + curr_str
        return curr_str
