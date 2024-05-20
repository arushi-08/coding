class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                digit1 = stack.pop()
                digit2 = stack.pop()
                stack.append(digit1 + digit2)
            elif tokens[i] == '-':
                digit1 = stack.pop()
                digit2 = stack.pop()
                stack.append(digit2 - digit1)
            elif tokens[i] == '*':
                digit1 = stack.pop()
                digit2 = stack.pop()
                stack.append(digit1 * digit2)
            elif tokens[i] == '/':
                digit1 = stack.pop()
                digit2 = stack.pop()
                stack.append(int(digit2 / digit1))
            else:
                stack.append(int(tokens[i]))
            # print('stack', stack)
        return stack.pop()
