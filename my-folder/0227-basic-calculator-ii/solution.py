class Solution:
    def calculate(self, s: str) -> int:
        
        op = '+'
        num = 0
        stack = []
        for c in s+'+':
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                pass
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    elem = stack.pop()
                    stack.append(num*elem)
                else:
                    elem = stack.pop()
                    stack.append(int(elem/num))
                num = 0
                op = c
        return sum(stack)

