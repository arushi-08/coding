class Solution:
    def calculate(self, s: str) -> int:
        """
        sign-stack algo
        use res, stack and sign variable
        when number is found -> res += number * sign
        when + found -> sign = 1
        when - found -> sign = -1
        when ( found -> push sign to stack
        when ) found -> pop from stack
        """

        s = s.replace(' ', '')

        res = 0
        stack = [1]
        sign = 1

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i += 1
            
                res += num * sign
            
            elif s[i] == '+':
                sign = stack[-1]
                i += 1

            elif s[i] == '-':
                sign = stack[-1] * (-1)
                i += 1
            
            elif s[i] == '(':
                stack.append(sign)
                i += 1
            
            else:
                sign = stack.pop()
                i += 1

        return res

